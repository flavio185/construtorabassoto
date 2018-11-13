from rest_framework.serializers import ModelSerializer
from funcionarios.models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'data_nascimento', 'rg', 'vale_transporte', 'vale_refeicao', 'ocupacao', 'cpf', 'endereco', 'cidade', 'estado','telefone', 'telefone2', 'email', 'ativo', 'imagem')
        #fields = ('id','nome') 