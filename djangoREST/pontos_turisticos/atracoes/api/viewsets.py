from rest_framework import viewsets
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
#from django_filters.rest_framework import DjangoFilterBackend


class AtracaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #ativando filtro.
    filter_fields = [ 'nome', 'descricao' ]