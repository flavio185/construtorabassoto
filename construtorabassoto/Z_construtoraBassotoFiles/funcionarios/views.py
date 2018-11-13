from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from decimal import *

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import FuncionarioForm, OcupacaoForm
from .models import Funcionario, Ocupacao

from django.contrib.auth.decorators import login_required

#import sum para soma de notas
from django.db.models import Sum

from django.contrib.auth.decorators import permission_required

# Create your views here.

"""
##############################################
#
Views relacionadas com Funcionarios.
#
##############################################
"""
"""
    Cria novo funcionario
"""
@login_required
def funcionario_novo(request):
    if request.method == "POST": 
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('funcionarios:funcionario_list'))

    else:
        form = FuncionarioForm()
    return render(request, 'funcionarios/funcionario_novo.html', {'form': form})    

"""
    Lista funcionarios
"""
@login_required
def funcionario_list(request):
    #if request.method == "GET":
    if 'ativo' in request.GET and request.GET['ativo']:
        status_func = request.GET['ativo']
        funcionarios = Funcionario.objects.filter(ativo=status_func)
        funcionarios = funcionarios.order_by('nome')
    else:
        status_func="True"
        funcionarios = Funcionario.objects.all()
        funcionarios = funcionarios.order_by('nome')
        funcionarios = funcionarios.filter(ativo=status_func)
    total_salarios = funcionarios.aggregate(Sum('ocupacao__valor'))
    total_salarios = total_salarios['ocupacao__valor__sum']
    #
    total_salarios_40pc =   total_salarios*Decimal(0.4)
    total_salarios_60pc =   total_salarios*Decimal(0.6)
    #
    total_alimentacao =   funcionarios.aggregate(Sum('vale_refeicao__valor'))
    total_alimentacao =   total_alimentacao['vale_refeicao__valor__sum']
    #
    total_transporte =   funcionarios.aggregate(Sum('vale_transporte__valor'))
    total_transporte =   total_transporte['vale_transporte__valor__sum']
    
    context = {
            'funcionarios': funcionarios,
            'status_func': status_func,
            'total_salarios': total_salarios,
            'total_salarios_40pc': total_salarios_40pc,
            'total_salarios_60pc': total_salarios_60pc,
            'total_alimentacao': total_alimentacao,
            'total_transporte': total_transporte
    }
    return render(request, 'funcionarios/funcionario_list.html', context)

"""
    Edita funcionarios.
"""
@login_required
def funcionario_edit(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('funcionarios:funcionario_list'))
            #next = request.POST.get('next', '/')
            #return HttpResponseRedirect(next)
    else:
        form = FuncionarioForm(instance=funcionario)
        pk = pk
    
    context = {'form': form, 
                    'pk': pk}

    return render(request, 'funcionarios/funcionario_edit.html', context)

"""
    Deleta funcionario.
"""
def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    return HttpResponseRedirect(reverse('notas:funcionario_list'))



"""
##############################################
#
Views relacionadas com Ocupacoes.
#
##############################################
"""
"""
    Cria novo funcionario
"""
@login_required
def ocupacao_nova(request):
    if request.method == "POST":
        form = OcupacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('funcionarios:ocupacao_list'))

    else:
        form = OcupacaoForm()
    return render(request, 'funcionarios/ocupacao/ocupacao_nova.html', {'form': form})    

"""
    Lista ocupacoes
"""
@login_required
def ocupacao_list(request):
    ocupacoes = Ocupacao.objects.all()
    ocupacoes = ocupacoes.order_by('nome')
    context = {'ocupacoes': ocupacoes}
    return render(request, 'funcionarios/ocupacao/ocupacao_list.html', context)

"""
    Edita ocupacoes.
"""
@login_required
def ocupacao_edit(request, pk):
    ocupacao = get_object_or_404(Ocupacao, pk=pk)
    if request.method == "POST":
        form = OcupacaoForm(request.POST, request.FILES, instance=ocupacao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('funcionarios:ocupacao_list'))
            #next = request.POST.get('next', '/')
            #return HttpResponseRedirect(next)
    else:
        form = OcupacaoForm(instance=ocupacao)
        pk = pk
    
    context = {'form': form, 
                    'pk': pk}

    return render(request, 'funcionarios/ocupacao/ocupacao_edit.html', context)

"""
    Deleta ocupacao.
"""
def ocupacao_delete(request, pk):
    ocupacao = get_object_or_404(Ocupacao, pk=pk)
    ocupacao.delete()
    return HttpResponseRedirect(reverse('funcionarios:ocupacao_list'))
