from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico

from .serializers import PontoTuristicoSerializer




class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    #ativando search field.
    filter_backends = (SearchFilter,)
    search_fields = ('=nome', 'descricao', '^endereco__linha1')
    #lookup field - buscasr por outro campo que não seja ID.
    lookup_field = 'nome'
    
    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)
        
        return queryset

    #def list(self, request, *args, **kwargs):
    #    return super(PontoTuristicoViewSet, self).list( request, *args, **kwargs )

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create( request, *args, **kwargs )

    #def destroy(self, request, *args, **kwargs):
    #    pass

    #def retrieve(self, request, *args, **kwargs):
    #    pass

    #def update(self, request, *args, **kwargs):
    #    pass

    #def partial_update(self, request, *args, **kwargs):
    #    pass
    
    @action(methods=['get'], detail=True)
    def denunciar( self, request, pk=None ):
        print('chegou')
        pass
