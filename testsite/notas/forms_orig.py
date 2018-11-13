from django import forms
from django.forms import ModelChoiceField
from .models import Nota, Deposito, Projeto, ServicoTerceirizado, EmpresaServico
from django.conf import settings


class NotaForm(forms.ModelForm):
    projeto = ModelChoiceField(Projeto.objects.all(), empty_label="Selecione o projeto")
    
    class Meta:
        model = Nota
        fields = ['numero', 'data', 'emitente', 'descricao', 'valor', 'tipo_gasto', 'projeto','deposito', 'imagem', 'imagem1']
        #fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['deposito'].queryset = Deposito.objects.none()

"""
Comentando função que verifica se numero da nota ja existe.
Esta dando problema quendo vai atualizar nota. Ele acha que a nota ja existe. e da erro.
    def clean_numero(self):
        # pega numero da nota digitado
        numero = self.cleaned_data.get('numero')
        pk = Nota.pk
        print("self.pk", pk)
        if self.cleaned_data.get('pk') is not None:
            return numero

        #Abre excessao para duplicadas
        if numero == 'RECIBO':
            return numero
        if numero == 'DEBITO':
            return numero
        ########

        # verifica se ja existe uma nota com esse numero.
        try:
            match = Nota.objects.get(numero=numero)
        except Nota.DoesNotExist:
            # nao encontrou nota com esse numero(ok).
            return numero

        # encontrou a nota com o mesmo numero. retorna mensagem.
        raise forms.ValidationError('Uma nota com esse número já foi lançada anteriormente.')

"""
#class NotaFilterForm(forms.Form):
#    data_inicio = forms.DateField()

class DepositoForm(forms.ModelForm):

    class Meta:
        model = Deposito
        fields = ['projeto', 'data', 'valor', 'comentarios']
        

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = ['nome']
        

class ServicoTerceirizadoForm(forms.ModelForm):

    class Meta:
        model = ServicoTerceirizado
        fields = ['data', 'empresa', 'descricao', 'valor', 'imagem', 'projeto']

class EmpresaServicoForm(forms.ModelForm):

    class Meta:
        model = EmpresaServico
        fields = ['nome', 'contato', 'telefone', 'telefone2', 'email', 'descricao', 'imagem']
        