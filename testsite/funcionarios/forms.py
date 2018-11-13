from django import forms
from django.forms import ModelChoiceField
from .models import Funcionario, Ocupacao, ValeRefeicao, ValeTransporte, Pagamento
from django.conf import settings


class FuncionarioForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome', 'class':'form-control'}),
            'data_nascimento': forms.TextInput(attrs={'type': 'date', 'class':'form-control'}),
            'rg': forms.TextInput(attrs={'placeholder': 'nn.nnn.nn.nnn-n', 'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'nnn.nnn.nnn-nn', 'class':'form-control'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Digite o endereço do funcionario.', 'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Digite o nome da cidade', 'class':'form-control'}),
            'estado': forms.TextInput(attrs={'placeholder': 'Ex.: SP', 'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(nn) nnnn-nnnn', 'class':'form-control'}),
            'telefone2': forms.TextInput(attrs={'placeholder': '(nn) nnnn-nnnn', 'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite o email', 'class':'form-control'}),
            'ocupacao': forms.Select(attrs={ 'class':'form-control'}),
            'vale_refeicao': forms.Select(attrs={ 'class':'form-control'}),
            'vale_transporte': forms.Select(attrs={ 'class':'form-control'}),
            'ativo': forms.CheckboxInput(attrs={}),
        }
        labels = {
            'telefone': 'Celular',
            'telefone2': 'Telefone',
            'ocupacao': 'Ocupação',
            'data_nascimento': 'Data de Nascimento',
            'vale_refeicao': 'Vale Refeição',
            'vale_transporte': 'Vale Transporte',

        }
        fields = ['nome', 'data_nascimento', 'rg', 'vale_transporte', 'vale_refeicao', 'ocupacao', 'cpf', 'endereco', 'cidade', 'estado','telefone', 'telefone2', 'email', 'ativo', 'imagem']

class OcupacaoForm(forms.ModelForm):
    class Meta:
        model = Ocupacao
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome da ocupação', 'class':'form-control'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Digita o valor', 'class':'form-control'}),
        }
        labels = {
            'nome': 'Ocupação',
            'valor': 'Valor',
        }
        fields = ['nome', 'valor']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        widgets = {
            'data': forms.TextInput(attrs={'type': 'date', 'class':'form-control'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Digite o valor', 'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Ex.: Adiantamento, Vale Transporte...', 'class':'form-control'}),
            'comentario': forms.TextInput(attrs={'placeholder': 'Caso necessário, informe detalhes do pagamento', 'class':'form-control'}),
        }
        '''labels = {
            'nome': 'Ocupação',
            'valor': 'Valor',
        }'''
        fields = [ 'data', 'valor', 'tipo', 'comentario' ]

class ValeRefeicaoForm(forms.ModelForm):
    class Meta:
        model = ValeRefeicao
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite um nome para identificação do VR', 'class':'form-control'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Digite o valor mensal do VR', 'class':'form-control'}),
        }
        labels = {
            'nome': 'Identificação',
            'valor': 'Valor',
        }
        fields = ['nome', 'valor']

class ValeTransporteForm(forms.ModelForm):
    class Meta:
        model = ValeTransporte
        widgets = {
            'valor': forms.NumberInput(attrs={'placeholder': 'Digita o valor do VT', 'class':'form-control'}),
        }
        labels = {
            'valor': 'Valor',
        }
        fields = ['valor',]