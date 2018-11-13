from django.contrib import admin

from .models import Nota, Projeto, ServicoTerceirizado, EmpresaServico
# Register your models here.

admin.site.register(Nota)
admin.site.register(Projeto)
admin.site.register(ServicoTerceirizado)
admin.site.register(EmpresaServico)


