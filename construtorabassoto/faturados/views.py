from django.shortcuts import render, get_object_or_404, resolve_url
from django.views.generic.list import View

from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from faturados.models import Faturado
from notas.models import Projeto


    

class FaturadoView(View):

    def home(request):
        return render(request, 'faturados/faturados_list.html')
        
    # def get(self, request):
    #     faturados =  Faturado.objects.all()
    #     context = {
    #         'faturados': faturados,
    #     }
    #     return render(request, "faturados/faturados_list.html", context)

    def get(self, request):
        f = Faturado.objects.all().order_by('-vencimento')
  
        pageN = 0 if request.GET.get('page') is None  else int(request.GET.get('page')) 
        meupaginador = myPaginator(f, pageN)
        page = meupaginador.get_page() 
        links=meupaginador.get_links()
        dictPages = meupaginador.dPages()

        return JsonResponse(dict(links=links, faturados=page, pages=dictPages))

    def getProjetos(self):
        projetos = Projeto.objects.all()
        json = [ dict(
            nome = p.nome,
            id = p.id
        ) for p in projetos
        ]
        return JsonResponse(dict(projetos=json))

class FaturadoDetail(View):

    def get(self, request, pk):
        faturado = get_object_or_404(Faturado, pk=pk)
        response = dict(
            vencimento=faturado.vencimento,
            descricao=faturado.descricao,
            valor=faturado.valor,
            projeto=faturado.projeto.nome,
            pago=faturado.pago,
        )

        return JsonResponse(response)
 
    def post(self, request, pk):

        faturado = Faturado.objects.get(pk=pk)
        print(request.POST)

        if 'altera_pago' in request.POST :
            if request.POST.get('altera_pago') == 'true':
                status = True
            else:
                status = False

            faturado.pago = status
        else:
            data = (request.POST.get(key) for key in ('vencimento', 'descricao', 'valor', 'pago'))   
            faturado.vencimento, faturado.descricao, faturado.valor,  faturado.pago = data

            proj =  {
            key: value for key, value in request.POST.items()
            if key in ('projeto')   
            }
            p = Projeto.objects.get(pk=proj['projeto'])
            #data.pop('projeto', None)
            
            #faturado = Faturado(**data)
            faturado.projeto = p
        
        faturado.save()

        response = dict(
            vencimento=faturado.vencimento,
            descricao=faturado.descricao,
            valor=faturado.valor,
            projeto=faturado.projeto.nome,
            pago=faturado.pago,
        )

        return JsonResponse(response)

        
class FaturadoCreate(View):

    def get(self, request):
        return HttpResponseNotAllowed(('POST',)) 

    def post(self, request):
        data = {
            key: value for key, value in request.POST.items()
            if key in ('vencimento', 'descricao', 'valor', 'projeto', 'pago')   
        }
        p = Projeto.objects.get(pk=data['projeto'])
        data.pop('projeto', None)
        
        faturado = Faturado(**data)
        faturado.projeto = p
        faturado.save()

        response = dict(
            vencimento=faturado.vencimento,
            descricao=faturado.descricao,
            valor=faturado.valor,
            projeto=faturado.projeto.nome,
            pago=faturado.pago,
        )

        return JsonResponse(response, status=201)
    


    #def paginate(self, objetos)?

def jsonizeQueryString(querystring):
    json = [ dict(
    vencimento = faturado.vencimento,
    descricao = faturado.descricao,
    valor = faturado.valor,
    projeto = str(faturado.projeto),
    pago = faturado.pago,
    url = resolve_url('faturados:faturado_detail', pk=faturado.pk)
    ) for faturado in querystring
    ]
    return json


class myPaginator:

    def __init__(self, object_list, num_pagina):
        self.object_list = object_list
        self.dictPages = self.dPages()
        self.num_pagina = int(num_pagina)

    def validate_page(self, number):
        """Validate the given 1-based page number."""
        try:
            number = int(number)
        except (TypeError, ValueError):
            #print('O número da página não é um inteiro.')
            pass
        if number < 1:
            #print('O número da p´´agina é menor que 1.')
            pass
        if number > self.num_pages():
                #print('That page contains no results')
                return 0
        return number

    def __repr__(self):
        return '<Page %s of %s>' % (self.num_pagina, self.num_pages())

    def count(self):
        """Return the total number of objects, across all pages."""
        try:
            return self.object_list.count()
        except (AttributeError, TypeError):
            # AttributeError if object_list has no count() method.
            # TypeError if object_list.count() requires arguments
            # (i.e. is of type list).
            return len(self.object_list)
    
    def dPages(self):
        """
        Retorna dict com cada pagina por mes/ano
        """
        #fVencimento = self.object_list.values('vencimento')
        dictDatas = {}
        for i in self.object_list.values('vencimento'):
            mesAno = str(i['vencimento'].month).zfill(2) + ' '+ str(i['vencimento'].year)
            #dictDatas[i['vencimento'].month] = i['vencimento'].year
            dictDatas[mesAno] = ''

        """newDictDatas={}
        i=1
        for mesAno, l in dictDatas.items():
            newDictDatas[i] = dict(mes=mesAno.split()[0], ano=mesAno.split()[1])
            i+=1"""
        
        newDictDatas=[]
        for mesAno, l in dictDatas.items():
            newDictDatas.append(dict(mes=mesAno.split()[0], ano=mesAno.split()[1]))

        return newDictDatas

    def num_pages(self):
        return len(self.dictPages)-1

    def get_page(self):
        pages = self.dictPages
        myPages = self.object_list.filter(vencimento__month=pages[self.num_pagina]['mes'])
        myPages = myPages.filter(vencimento__year=pages[self.num_pagina]['ano']).order_by('vencimento')
        serializable = jsonizeQueryString(myPages)
        return serializable
    
    def get_self(self):
        return self.num_pagina

    def get_first(self):
        return 0
    
    def get_prev(self):
        return self.validate_page(self.num_pagina-1)

    def get_next(self):
        return self.validate_page(self.num_pagina+1)

    def get_last(self):
        return self.num_pages()

    def get_links(self):
        links = dict([
            ('self', self.get_self()),
            ('first', self.get_first()),
            ('last', self.get_last()),
            ('next', self.get_next()),
            ('prev', self.get_prev())
        ])

        return links


    #def has_next(self):


    #def pages(self):