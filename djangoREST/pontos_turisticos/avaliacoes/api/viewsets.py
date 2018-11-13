from rest_framework import viewsets
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer