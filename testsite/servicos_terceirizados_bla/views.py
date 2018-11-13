from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import ServicoTerceirizadoForm, EmpresaServicoForm
from .models import ServicoTerceirizado, EmpresaServico
from notas.models import Nota

from django.contrib.auth.decorators import login_required

#import sum para soma de notas
from django.db.models import Sum

from django.contrib.auth.decorators import permission_required

# Create your views here.
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
            return HttpResponseRedirect(reverse('servicos_terceirizados:servico_list'))

    else:
        form = ServicoTerceirizadoForm()
    return render(request, 'servicos/servico_novo.html', {'form': form})    

"""
    Lista servicos
"""
@login_required
def servico_list(request):
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
        notas = Nota.objects.filter(servico_terceirizado=pk)
        context = {
            'form': form, 
            'media_url':"/media/",
            'pk': pk,
            'notas': notas
            }

    return render(request, 'servicos/servico_edit.html', context)

"""
    Deleta ServicoTerceirizado.
"""
def servico_delete(request, pk):
    servico_terceirizado = get_object_or_404(ServicoTerceirizado, pk=pk)
    servico_terceirizado.delete()
    return HttpResponseRedirect(reverse('servicos_terceirizados:servico_list'))

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
    return render(request, 'empresas/empresa_nova.html', {'form': form})    


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
    return render(request, 'empresas/empresa_list.html', context)

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

    return render(request, 'empresas/empresa_edit.html', context)

"""
    Deleta Empresa Servico.
"""
def empresa_delete(request, pk):
    empresa_servico = get_object_or_404(EmpresaServico, pk=pk)
    empresa_servico.delete()
    return HttpResponseRedirect(reverse('servicos_terceirizados:empresa_list'))

