from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import NotaForm, DepositoForm
from .models import Nota, Deposito

from django.contrib.auth.decorators import login_required

#import sum para soma de notas
from django.db.models import Sum


# Create your views here.

#class CriaNota(CreateView):
#    model = NotasCompra
    #fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto', 'imagem', 'imagem1'] 
#    fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto'] 
#    template_name = "adiciona-nota.html"
 
# Create your views here.
"""
    View que lista notas.
"""
@login_required
def nota_list(request):
    deposito = Deposito.objects.all()[0]
    notas = Nota.objects.all()
    notas = notas.filter(deposito=deposito)

    total_notas = notas.aggregate(Sum('valor'))
    total_notas = total_notas['valor__sum']
    #dep = dep.valor
    valor_em_caixa = deposito.valor - total_notas
    
    #seach box#
    #args = {}
    #args.update(csrf(request))
    #
    context = {'notas': notas, 
                'deposito':deposito, 
                'valor_em_caixa': valor_em_caixa, 
                'total_notas':total_notas, 
                'media_url':"/media/"}

    return render(request, 'notas/nota_list.html', context)




"""
    View que recebe Post com filtros, faz query no banco e renderiza a pagina em nota_list
"""
def nota_filter(request):
    #form = UserQueryForm(request.POST)
    notas = Nota.objects.all()
    query = "Nota.objects.all()"


    

    if 'data_inicio' in request.GET and request.GET['data_inicio']:
        #message = 'You searched for: %r' % request.GET['data_inicio']
        data_inicio = request.GET['data_inicio']
        notas = notas.filter(data__gte=data_inicio)
        query += ".filter(data__gte='"+data_inicio+"')"

    if 'data_fim' in request.GET and request.GET['data_fim']:
        #message = 'You searched for: %r' % request.GET['data_inicio']
        data_fim = request.GET['data_fim']
        notas = notas.filter(data__lte=data_fim)
        query += ".filter(data__lte='"+data_fim+"')"
    
    if 'valor' in request.GET and request.GET['valor']:
        valor = request.GET['valor']
        notas = notas.filter(valor=valor)
        query += ".filter(valor='"+valor+"')"
    
    if 'deposito' in request.GET and request.GET['deposito']:
        deposito = request.GET['deposito']
        notas = notas.filter(deposito_id=deposito)
        query += ".filter(deposito_id='"+deposito+"')"
        #Calcula valor em caixa
        deposito = Deposito.objects.get(pk=deposito)
    else:
        #Se deposito não foi excolhido, Seta variaveis como nulo
        deposito=""
        valor_em_caixa=""
        total_notas=""
        
    if 'tipo_gasto' in request.GET and request.GET['tipo_gasto']:
        tipo_gasto = request.GET['tipo_gasto']
        notas = notas.filter(tipo_gasto=tipo_gasto)
        query += ".filter(tipo_gasto='"+tipo_gasto+"')"
    
    try:
        total_notas = notas.aggregate(Sum('valor'))
        total_notas = total_notas['valor__sum']

    except:
        total_notas="Pesquisa não retornou nota."
        
    
    try:
        valor_em_caixa = deposito.valor - total_notas
    except:
        valor_em_caixa=""
    
    context = {'notas': notas, 
                'query': query, 
                'deposito':deposito, 
                'valor_em_caixa': valor_em_caixa, 
                'total_notas':total_notas,
                'media_url':"/media/"}
    
    return render(request, 'notas/nota_list.html', context)
        
    #else:
    #    message = 'You submitted an empty form.'
    #return HttpResponse(message)

"""
    View que carrega form para filtro de notas.
"""
def nota_filter_form(request):
    depositos = Deposito.objects.all()
    context = {'depositos': depositos}
    return render(request, 'notas/nota_filter_form.html', context)


"""
    view que carrega form e salva notas imputadas.
"""
def nota_nova(request):
    if request.method == "POST":
        form = NotaForm(request.POST, request.FILES)
        if form.is_valid():
            #numero = form.cleaned_data['numero']
            #data = form.cleaned_data['data']
            #descricao = form.cleaned_data['descricao']
            #valor = form.cleaned_data['valor']
            #tipo_gasto = form.cleaned_data['tipo_gasto']
            form.save()
            return HttpResponseRedirect(reverse('notas:nota_list'))
    else:
        form = NotaForm()
    return render(request, 'notas/nota_nova.html', {'form': form})    

"""
    View que recebe como parametro nota e faz edição dela.
"""
def nota_edit(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, request.FILES, instance=nota)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notas:nota_list'))
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/nota_edit.html', {'form': form})

"""
    mostra detalhes da nota
"""
def nota_detalhes(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    return render(request, 'notas/nota_detalhes.html', {'nota': nota})

"""
    salva query para usuário. (decomission in progress.)
"""
#salva query para colocar na home page dos usuarios. especifico pra cada usuario.
def save_query_to_user(request):
    if request.method == "POST":
        form = UserQueryForm(request.POST)
        print(form)
        if form.is_valid():
            #query = form.cleaned_data['query']
            print("bla")
            #usuario = form.cleaned_data['usuario']
            form.save()
            #return redirect('notas/nota_list.htm')
            return HttpResponse('Hello World, salvou!!!')
    else:
        form = UserQueryForm()
#corrigir aqui.
    #return render(request, 'notas/nota_list.html')
    return HttpResponse('nada!!!')

####################
#
#Teste model  QueryUser. passando usuario alias e query.
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
###############
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class QueryUserListView(LoginRequiredMixin, generic.ListView):
    
    #Generic class-based view listing queries for current user. 
    
    model = UserQuery
    context_object_name = 'minhas_notas'  
    template_name ='notas/saved_user_query_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return UserQuery.objects.filter(user=self.request.user)
"""
#
#
#
###################################
"""
Views relacionadas com Depósitos.
"""
#Cria novo deposito.
def deposito_novo(request):
    if request.method == "POST":
        form = DepositoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notas/deposito_detalhes.html', pk=numero.pk)
    else:
        form = DepositoForm()
    return render(request, 'notas/deposito_edit.html', {'form': form})    

"""
    Lista depositos
"""
@login_required
def deposito_list(request):
    depositos = Deposito.objects.all()
    context = {'depositos': depositos}
    return render(request, 'notas/deposito_list.html', context)

"""
from .forms import newNotaForm

def newNota(request):
    if request.method == "POST":
        form = newNotaForm(request.POST, request.FILES)
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            numero = form.cleaned_data['numero']
            data = form.cleaned_data['data']
            emitente = form.cleaned_data['emitente']
            descricao = form.cleaned_data['descricao']
            valor = form.cleaned_data['valor']
            tipo_gasto = form.cleaned_data['tipo_gasto']
            deposito = form.cleaned_data['tipo_gasto']
            imagem = form.cleaned_data['imagem']
            imagem1 = form.cleaned_data['imagem1']

            form.save()
            return HttpResponseRedirect(reverse('notas:nota_list'))
    else:
        form = newNotaForm()
    return render(request, 'notas/nota_edit.html', {'form': form})
"""
