from rest_framework import viewsets
from funcionarios.models import Funcionario
from .serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    serializer_class = FuncionarioSerializer

    def get_queryset(self):
        ativo = self.request.query_params.get('ativo', None)
        queryset = Funcionario.objects.all()
        
        if ativo:
            queryset = queryset.filter(ativo=ativo)
            #queryset = queryset.order_by('nome')

        return queryset

    