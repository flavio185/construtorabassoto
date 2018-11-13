"""
funcionarios URL Configuration
"""
from django.conf.urls import url
from django.urls import path


from . import views

app_name = 'funcionarios'

urlpatterns = [
    #Funcionarios
    path('novo/', views.funcionario_novo, name='funcionario_novo'),
    path('list/', views.funcionario_list, name='funcionario_list'),
    path('<int:pk>/edit/', views.funcionario_edit, name='funcionario_edit'),
    path('<int:pk>/delete/', views.funcionario_delete, name='funcionario_delete'),
    #Ocupações
    path('ocupacao/nova/', views.ocupacao_nova, name='ocupacao_nova'),
    path('ocupacao/list/', views.ocupacao_list, name='ocupacao_list'),
    path('ocupacao/<int:pk>/edit/', views.ocupacao_edit, name='ocupacao_edit'),
    path('ocupacao/<int:pk>/delete/', views.ocupacao_delete, name='ocupacao_delete'),
    #Pagamentos
    path('pagamento/novo/', views.pagamento_novo, name='pagamento_novo'),
    path('pagamento/list/', views.pagamento_list, name='pagamento_list'),
    path('pagamento/<int:pk>/edit/', views.pagamento_edit, name='pagamento_edit'),
    #path('pagamento/<int:pk>/delete/', views.pagamento_delete, name='pagamento_delete'),    
 
    
]
