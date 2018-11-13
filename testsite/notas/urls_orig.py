"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path


from . import views

#urlpatterns = [
#    url(r'^nova/$', views.nota_nova, name='nota_nova'),
#    url(r'^(?P<pk>\d+)/edit/$', views.nota_edit, name='nota_edit'),
#]

app_name = 'notas'

urlpatterns = [
    path('', views.nota_list, name='nota_list'),
    path('nova/', views.nota_nova, name='nota_nova'),
    path('<int:pk>/edit/', views.nota_edit, name='nota_edit'),
    path('<int:pk>/delete/', views.nota_delete, name='nota_delete'),
    path('<int:pk>', views.nota_detalhes, name='nota_detalhes'),
    path('nota_filter_form/', views.nota_filter_form, name='nota_filter_form'),
    path('nota_filter/', views.nota_filter, name='nota_filter'),
    #Depósitos
    path('deposito/deposito_novo/', views.deposito_novo, name='deposito_novo'),
    path('deposito/deposito_list/', views.deposito_list, name='deposito_list'),
    path('<int:pk>/deposito/edit/', views.deposito_edit, name='deposito_edit'),
    path('<int:pk>/deposito/delete/', views.deposito_delete, name='deposito_delete'),
    path('notas/carregar-depositos/', views.carregar_depositos, name='ajax_carregar_depositos'),  # <-- this one here
    #Serviços terceirizados
    path('serv_terc/servico_novo/', views.servico_novo, name='servico_novo'),
    path('serv_terc/servico_list/', views.servico_list, name='servico_list'),
    path('serv_terc/<int:pk>/edit/', views.servico_edit, name='servico_edit'),
    path('serv_terc/<int:pk>/delete/', views.servico_delete, name='servico_delete'),
    #path('serv_terc/<int:pk>/notas/', views.servico_nota, name='servico_nota'),
    #Empresa terceirizada
    path('empresa_servico/empresa_nova/', views.empresa_nova, name='empresa_nova'),
    path('empresa_servico/empresa_list/', views.empresa_list, name='empresa_list'),
    path('empresa_servico/<int:pk>/edit/', views.empresa_edit, name='empresa_edit'),
    path('empresa_servico/<int:pk>/delete/', views.empresa_delete, name='empresa_delete'),  
    #path('minhas_notas/', views.QueryUserListView.as_view(), name='minhas_notas'),
    #path('newNota/', views.newNota, name='newNota'),
    
]
