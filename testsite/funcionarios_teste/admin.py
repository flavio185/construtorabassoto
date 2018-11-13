from django.contrib import admin
from .models import Funcionario, Ocupacao, Pagamento
# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Ocupacao)
admin.site.register(Pagamento)
