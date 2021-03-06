from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    funcionarios = Funcionario.objects.all()
    funcionarios = funcionarios.order_by('nome')
    context = {'funcionarios': funcionarios}
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
            print(form)
            form.save()
            return HttpResponseRedirect(reverse('funcionarios:funcionario_list'))
            #next = request.POST.get('next', '/')
            #return HttpResponseRedirect(next)
    else:
        form = FuncionarioForm(instance=funcionario)
        pk = pk
    
    context = {'form': form, 
                    'pk': pk}

    return render(request, 'funcionarios_teste/funcionario_edit.html', context)

"""
    Ver funcionarios.
"""
@login_required
def funcionario_view(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect(reverse('funcionarios:funcionario_list'))
            #next = request.POST.get('next', '/')
            #return HttpResponseRedirect(next)
    else:
        form = FuncionarioForm(instance=funcionario)
        pk = pk
    
    context = {'form': form, 
                    'pk': pk}

    return render(request, 'funcionarios/funcionario_view.html', context)

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
            print(form)
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
