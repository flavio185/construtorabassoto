from rest_framework import viewsets
from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer