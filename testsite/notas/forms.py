from django import forms
from .models import Nota, UserQuery, Deposito
from django.conf import settings

class NotaForm(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ['numero', 'data', 'emitente', 'descricao', 'valor', 'tipo_gasto', 'deposito', 'imagem', 'imagem1']
        #fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto']

class newNotaForm(forms.Form):
    numero = forms.CharField(max_length=25, help_text="Insira o número da nota.")
    #data = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, help_text="Insira a data da nota.")
    data = forms.DateField( help_text="Insira a data da nota.")
    emitente = forms.CharField(max_length=25, help_text="Insira o emitente da nota.")
    descricao = forms.CharField(max_length=500, help_text="Insira uma descrição para a nota.")
    valor = forms.DecimalField(decimal_places=10, help_text="Insira o valor total da nota.")
    TIPO_GASTO = (
        ('', 'Selecione'),       
        ('Ferramentas', 'Ferramentas'),
        ('Serviços', 'Serviços'),
    )
    tipo_gasto = forms.ChoiceField(choices=TIPO_GASTO)
    deposito = forms.ModelChoiceField(queryset=Deposito.objects.all(), initial=0)
    imagem = forms.FileField(required=False)
    imagem1 = forms.FileField(required=False)

    def save(self):
        data = self.cleaned_data
        nota = Nota( 
            numero=data['numero'],
            data=data['data'],
            emitente=data['emitente'],
            descricao=data['descricao'],
            valor=data['valor'],
            tipo_gasto=data['tipo_gasto'],
            deposito=data['deposito'],
            imagem=data['imagem'],
            imagem1=data['imagem1']
        )
        nota.save()


    class Meta:
        model = UserQuery
        fields = ['user', 'query', 'alias']

#class NotaFilterForm(forms.Form):
#    data_inicio = forms.DateField()

class DepositoForm(forms.ModelForm):

    class Meta:
        model = Deposito
        fields = ['data', 'valor', 'comentarios']
        


