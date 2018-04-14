from django.db import models

#import user model
from django.contrib.auth.models import User

# Create your models here.


#def f(instance, filename):
#    ext = filename.split('.')[-1]
#    if instance.numero:
#        return '{}{}.{}'.format('notas_commpras/', instance.numero, ext)
#    else:
#        pass

class Nota(models.Model):
	"""
	Modelo representando pagamentos feitos, seja de funcionarios, serviços, materiais ou equipamentos.abs
    """
	numero = models.CharField(max_length=20)
	data = models.DateField(blank=True)
	emitente = models.CharField(max_length=30)
	descricao = models.CharField(max_length=70)
	valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	
	TIPO_GASTO = (
		('Serviços', 'SERVIÇOS'),
		('Ferramentas','FERRAMENTAS'),
	)

	tipo_gasto = models.CharField(max_length=12, choices=TIPO_GASTO)
	imagem = models.FileField( upload_to='notas_compras', blank=True,)
	imagem1 = models.FileField( upload_to='notas_compras', blank=True,)

	def deposito_corrente():
		return {Deposito.objects.last()}

	deposito = models.ForeignKey('Deposito', on_delete=models.SET_NULL, null=True, default=deposito_corrente)
	
	#methods
	def __str__(self):
		return '<Numero: {}, data: {}, imagem: {}>'.format(self.numero, self.data, self.imagem)

	
	#what todo after saving
	def save(self, *args, **kwargs):
		#captalize: deixa primeira letra maiuscula
		for field_name in [ 'tipo_gasto' ]:
			val = getattr(self, field_name, False)
			if val:
				setattr(self, field_name, val.capitalize())
       
		#important to call superclass method.
		#If you want the method to be called after is saved,
		#add yoiur lines after super method call
		super(Nota, self).save(*args, **kwargs)

	def image_url(self):
		"""
		Returns the URL of the image associated with this Object.
		If an image hasn't been uploaded yet, it returns a stock image

		:returns: str -- the image url

		"""
		if self.imagem and hasattr(self.imagem, 'url'):
			return self.imagem.url           
		else:
			return '/static/images/sample.jpg'

	def image1_url(self):
		if self.imagem1 and hasattr(self.imagem1, 'url'):
			return self.imagem1.url
		else:
			return '/static/images/sample.jpg'


class UserQuery(models.Model):

	query = models.CharField(max_length=150)
	alias = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Deposito(models.Model):
	"""
	Modelo representando depositos feitos pelo contratante do serviço. (pagamentos recebidos.)
	Esses depósitos terão referencia com as notas de compra.
	O valor dessas notas irão abater do valor total do deposito feito
	"""

	data = models.DateField()
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	comentarios = models.CharField(max_length=70, blank=True, help_text="Informações relacionadas com o depósito(opcional).")
	#methods
	def __str__(self):
		return '<Data: {}, Valor: {}>'.format(self.data, self.valor)
	
	def dinheiro_em_caixa(self):
		self.valor 

	class Meta:
		ordering = ["-id"]	
	