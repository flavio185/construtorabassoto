from django.conf.urls import url
from django.urls import path

from .views import FaturadoView, FaturadoDetail, FaturadoCreate

app_name = 'faturados'

urlpatterns = [
    path('', FaturadoView.home, name='home'),
    path('home', FaturadoView.home, name='home'),
    path('list/', FaturadoView.as_view(), name='faturado_list'),
    path('<int:pk>/detail', FaturadoDetail.as_view(), name='faturado_detail'),
    path('new/', FaturadoCreate.as_view(), name='faturado_create'),
    #Retorna projetos para popular form
    path('projetos/', FaturadoView.getProjetos, name='get_projetos'),

]