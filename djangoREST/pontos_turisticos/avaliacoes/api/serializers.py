from rest_framework import serializers
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'user', 'comentario', 'nota', 'data']
