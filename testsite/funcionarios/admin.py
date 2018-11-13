from django.contrib import admin
from .models import Funcionario, Ocupacao, Pagamento, ValeRefeicao, ValeTransporte
# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Ocupacao)
admin.site.register(ValeRefeicao)
admin.site.register(ValeTransporte)
admin.site.register(Pagamento)
