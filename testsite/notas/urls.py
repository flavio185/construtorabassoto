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
    path('<int:pk>', views.nota_detalhes, name='nota_detalhes'),
    path('nota_filter_form/', views.nota_filter_form, name='nota_filter_form'),
    path('nota_filter/', views.nota_filter, name='nota_filter'),
    path('save_query_to_user/', views.save_query_to_user, name='save_query_to_user'),
    path('deposito_novo/', views.deposito_novo, name='deposito_novo'),
    path('deposito_list/', views.deposito_list, name='deposito_list'),
    #path('minhas_notas/', views.QueryUserListView.as_view(), name='minhas_notas'),
    #path('newNota/', views.newNota, name='newNota'),
    
]
