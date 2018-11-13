from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import NotaForm, DepositoForm, ServicoTerceirizadoForm, EmpresaServicoForm
from .models import Nota, Deposito, Projeto, ServicoTerceirizado, EmpresaServico

from django.contrib.auth.decorators import login_required

#import sum para soma de notas
from django.db.models import Sum

from django.contrib.auth.decorators import permission_required


# Create your views here.

#class CriaNota(CreateView):
#    model = NotasCompra
#   fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto', 'imagem', 'imagem1'] 
#    fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto'] 
#    template_name = "adiciona-nota.html"
 
# Create your views here.
"""
    View que lista notas.
"""
@login_required
def nota_list(request):
    
    allProjetos = Projeto.objects.all()
    if 'projeto' in request.GET and request.GET['projeto']:
        get_projeto = request.GET['projeto']
        projetos = Projeto.objects.filter(nome=get_projeto)
        #projetos = Projeto.objects.get(id=projeto)
    else:
        try:
            #seleciona projetos
            projetos = Projeto.objects.order_by('-id')
        except:
            #nao existe projeto no sistema
            projetos="" 

    for projeto in projetos:
        try:
            #Seleciona depositos.
            deposito = Deposito.objects.filter(projeto_id=projeto.id)[0]
        except:
            #nao existe deposito no sistema
            deposito=""
        
        #Selectiona notas - sempre relacionadas com um projeto.
        notas = Nota.objects.filter(projeto_id=projeto.id)
        #filtra para mostrar notas relacionadas com o ultimo depósito.
        if deposito != "":
            #existe deposito no sistema.
            notas = notas.filter(deposito=deposito)
            if not notas:
                total_notas = "nenhuma nota"
                valor_em_caixa = "nenhuma nota"
            else:
                total_notas = notas.aggregate(Sum('valor'))
                total_notas = total_notas['valor__sum']
                #dep = dep.valor
                valor_em_caixa = deposito.valor - total_notas
        else:
            #nao existe deposito.
            deposito = ""
            total_notas = notas.aggregate(Sum('valor'))
            total_notas = total_notas['valor__sum']
            valor_em_caixa = total_notas
        

    context = { 'allProjetos': allProjetos,
                'projetos':projetos,
                'projeto':projeto,
                'notas': notas, 
                'deposito':deposito, 
                'valor_em_caixa': valor_em_caixa, 
                'total_notas':total_notas, 
                'media_url':"/media/"}

    return render(request, 'notas/nota_list.html', context)




"""
    View que recebe Post com filtros, faz query no banco e renderiza a pagina em nota_list
"""
@login_required
def nota_filter(request):
    #form = UserQueryForm(request.POST)
    notas = Nota.objects.all()
    query = "Nota.objects.all()"

    if 'projeto' in request.GET and request.GET['projeto']:
        #message = 'You searched for: %r' % request.GET['projeto']
        projeto = request.GET['projeto']
        notas = notas.filter(projeto=projeto)
        query += ".filter(projeto='"+projeto+"')"
        projeto = Projeto.objects.get(id=projeto)

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
    
    if 'numero' in request.GET and request.GET['numero']:
        numero = request.GET['numero']
        notas = notas.filter(numero=numero)
        query += ".filter(numero='"+numero+"')"

    if 'emitente' in request.GET and request.GET['emitente']:
        emitente = request.GET['emitente']
        notas = notas.filter(emitente=emitente)
        query += ".filter(emitente='"+emitente+"')"
    
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
    
    #notas = notas.filter(projeto_id=projeto.id)



    context = {'projeto': projeto,
                'notas': notas, 
                'query': query, 
                'deposito':deposito, 
                'valor_em_caixa': valor_em_caixa, 
                'total_notas':total_notas,
                'media_url':"/media/"}
    
    return render(request, 'notas/nota_list_filter.html', context)
        
    #else:
    #    message = 'You submitted an empty form.'
    #return HttpResponse(message)

"""
    View que carrega form para filtro de notas.
"""
@login_required
def nota_filter_form(request):
    projetos = Projeto.objects.all()
    depositos = Deposito.objects.none()
    context = {'depositos': depositos,
                'projetos': projetos}
    return render(request, 'notas/nota_filter_form.html', context)


"""
    view que carrega form e salva notas imputadas.
"""
@login_required
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
            
            return HttpResponseRedirect(reverse('notas:nota_nova'))
            #return render(request, 'notas/nota_detalhes.html', {'nota': nota})
    else:
        form = NotaForm()
    return render(request, 'notas/nota_nova.html', {'form': form})    

"""
    View que recebe como parametro nota e faz edição dela.
"""
@login_required
def nota_edit(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        form = NotaForm(request.POST, request.FILES, instance=nota)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('notas:nota_list'))
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = NotaForm(instance=nota)
        pk = pk
    context = {'form': form, 
                'pk': pk,
                'media_url':"/media/"}
                    
    return render(request, 'notas/nota_edit.html', context)

"""
    Deleta Nota.
"""
def nota_delete(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    nota.delete()
    return HttpResponseRedirect(reverse('notas:nota_list'))

"""
    mostra detalhes da nota
"""
@login_required
def nota_detalhes(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    return render(request, 'notas/nota_detalhes.html', {'nota': nota})

"""
##############################################
#
Views relacionadas com Depósitos.
#
##############################################
"""
"""
    Cria novo deposito
"""
@login_required
def deposito_novo(request):
    if request.method == "POST":
        form = DepositoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notas:deposito_list'))

    else:
        form = DepositoForm()
    return render(request, 'depositos/deposito_novo.html', {'form': form})    

"""
    Lista depositos
"""
@login_required
def deposito_list(request):
    depositos = Deposito.objects.all()
    depositos = depositos.order_by('-data')
    context = {'depositos': depositos}
    return render(request, 'depositos/deposito_list.html', context)

"""
    Edita depositos.
"""
@login_required
def deposito_edit(request, pk):
    deposito = get_object_or_404(Deposito, pk=pk)
    if request.method == "POST":
        form = DepositoForm(request.POST, request.FILES, instance=deposito)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('notas:deposito_list'))
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = DepositoForm(instance=deposito)
        pk = pk
        context = {'form': form, 
                    'pk': pk}

    return render(request, 'depositos/deposito_edit.html', context)

"""
    Deleta Deposito.
"""
def deposito_delete(request, pk):
    deposito = get_object_or_404(Deposito, pk=pk)
    deposito.delete()
    return HttpResponseRedirect(reverse('notas:deposito_list'))

"""
    View para carregamento dinamico de depositos.
"""
def carregar_depositos(request):
    projeto_id = request.GET.get('projeto')
    depositos = Deposito.objects.filter(projeto_id=projeto_id)
    return render(request, 'depositos/depositos_dropdown_list_options.html', {'depositos': depositos})

"""
##############################################
#
Views relacionadas com Serviços Terceirizados..
#
##############################################
"""
"""
    Cria novo servico_terceirizado
"""
@login_required
def servico_novo(request):
    if request.method == "POST":
        form = ServicoTerceirizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notas:servico_list'))

    else:
        form = ServicoTerceirizadoForm()
    return render(request, 'servicos/servico_novo.html', {'form': form})    

"""
    Lista servicos
"""
@login_required
def servico_list(request, ):
    servicos = ServicoTerceirizado.objects.all()
    servicos = servicos.order_by('-data')

    empresa = request.GET.get('empresa', None)
    #empresa = get_object_or_404(Deposito, pk=pk)
    if empresa:
        servicos = servicos.filter(empresa = empresa)

    if not servicos:
        #existe deposiservicosto no sistema.
        total_servicos = "nenhum serviço"
    else:
        total_servicos = servicos.aggregate(Sum('valor'))
        total_servicos = total_servicos['valor__sum']
        #nao existe deposito.

        
    context = {
        'servicos': servicos,
        'total_servicos': total_servicos,
        'media_url':"/media/"
        }
    return render(request, 'servicos/servico_list.html', context)

"""
    Edita servicos.
"""
@login_required
def servico_edit(request, pk):
    servico_terceirizado = get_object_or_404(ServicoTerceirizado, pk=pk)
    if request.method == "POST":
        form = ServicoTerceirizadoForm(request.POST, request.FILES, instance=servico_terceirizado)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('notas:servico_list'))
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = ServicoTerceirizadoForm(instance=servico_terceirizado)
        pk = pk
        context = {
            'form': form, 
            'media_url':"/media/",
            'pk': pk
            }

    return render(request, 'servicos/servico_edit.html', context)

"""
    Deleta ServicoTerceirizado.
"""
def servico_delete(request, pk):
    servico_terceirizado = get_object_or_404(ServicoTerceirizado, pk=pk)
    servico_terceirizado.delete()
    return HttpResponseRedirect(reverse('notas:servico_list'))

"""
##############################################
#
Views relacionadas com Empresas contratadas..
#
##############################################
"""
"""
    Cria novo servico_terceirizado
"""
@login_required
def empresa_nova(request):
    if request.method == "POST":
        form = EmpresaServicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)

    else:
        form = EmpresaServicoForm()
    return render(request, 'notas/empresa_nova.html', {'form': form})    


"""
    Lista servicos
"""
@login_required
def empresa_list(request):
    empresas = EmpresaServico.objects.all()
    empresas = empresas.order_by('nome')

    
    context = {
        'empresas': empresas,
        'media_url':"/media/"
        }
    return render(request, 'notas/empresa_list.html', context)

"""
    Edita empresas.
"""
@login_required
def empresa_edit(request, pk):
    empresa_servico = get_object_or_404(EmpresaServico, pk=pk)
    if request.method == "POST":
        form = EmpresaServicoForm(request.POST, request.FILES, instance=empresa_servico)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('notas:servico_list'))
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = EmpresaServicoForm(instance=empresa_servico)
        pk = pk
        context = {
            'form': form, 
            'pk': pk,
            'media_url':"/media/"
            }

    return render(request, 'notas/empresa_edit.html', context)

"""
    Deleta Empresa Servico.
"""
def empresa_delete(request, pk):
    empresa_servico = get_object_or_404(EmpresaServico, pk=pk)
    empresa_servico.delete()
    return HttpResponseRedirect(reverse('notas:empresa_list'))
