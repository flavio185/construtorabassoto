from rest_framework import viewsets
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer