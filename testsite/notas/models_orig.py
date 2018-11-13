from django.db import models

#import user model
from django.contrib.auth.models import User

# Create your models here.

class Nota(models.Model):
	"""
	Modelo representando pagamentos feitos, seja de funcionarios, serviços, materiais ou equipamentos.abs
    """
	numero = models.CharField(
		max_length=20
		)
	data = models.DateField(
		blank=True
		)
	emitente = models.CharField(
		max_length=30
		)
	descricao = models.CharField(
		max_length=70
		)
	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2, 
		blank=True
		)
	
	TIPO_GASTO = (
		('Materiais', 'MATERIAIS'),
		('Equipamentos','EQUIPAMENTOS'),
		('Serviços', 'SERVIÇOS'),
		('Funcionários', 'FUNCIONARIOS'),		
	)

	tipo_gasto = models.CharField(
		max_length=12, 
		choices=TIPO_GASTO
		)
	
	projeto = models.ForeignKey(
		'Projeto', 
		on_delete=models.SET_NULL, 
		null=True
		)

	imagem = models.FileField( 
		upload_to='notas_compras', 
		blank=True,
		)
	imagem1 = models.FileField( 
		upload_to='notas_compras', 
		blank=True,
		)
	servico_terceirizado = models.ForeignKey(
		'ServicoTerceirizado',
		on_delete=models.SET_NULL, 
		null=True, 
		blank=True
		)

	def deposito_corrente():
		return {Deposito.objects.last()}

	deposito = models.ForeignKey(
		'Deposito', 
		on_delete=models.SET_NULL, 
		null=True, 
		default=deposito_corrente
		)

	
	class Meta:
		permissions = (("can_change", "Pode alterar notas"),)
		ordering = ["data"]	
	
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


class Deposito(models.Model):
	"""
	Modelo representando depositos feitos pelo contratante do serviço. (pagamentos recebidos.)
	Esses depósitos terão referencia com as notas de compra.
	O valor dessas notas irão abater do valor total do deposito feito
	"""

	data = models.DateField()
	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2
		)
	comentarios = models.CharField(
		max_length=70, 
		blank=True, 
		help_text="Informações relacionadas com o depósito(opcional)."
		)
	#FK projetos
	projeto = models.ForeignKey(
		'Projeto', 
		on_delete=models.SET_NULL, 
		null=True)
	#methods
	
	def __str__(self):
		return 'Data: {}, Valor: {}'.format(self.data, self.valor)
	
	def dinheiro_em_caixa(self):
		self.valor 

	class Meta:
		ordering = ["-id"]	

class Projeto(models.Model):
	nome = models.CharField(
		max_length=30
		)

	def __str__(self):
		#return 'Nome: {}'.format(self.nome)
		return self.nome


class ServicoTerceirizado(models.Model):
	data = models.DateField(
		blank=True
		)
	descricao = models.CharField(
		max_length=150
		)
	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2, 
		blank=True
		)
	imagem = models.FileField( 
		upload_to='servicos_terceirizados', 
		blank=True
		)
	#FK projetos
	projeto = models.ForeignKey(
		'Projeto', 
		on_delete=models.SET_NULL, 
		null=True
		)
	
	#FK empresa	
	empresa = models.ForeignKey(
		'EmpresaServico', 
		on_delete=models.SET_NULL, 
		null=True
		)

	def __str__(self):
		return 'Data: {}, Valor: {}'.format(self.data, self.valor)

class EmpresaServico(models.Model):
	nome = models.CharField(
		max_length=40
		)
	contato = models.CharField(
		max_length=30
	)
	telefone = models.CharField(
	    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
		#validators=[phone_regex], 
		max_length=17, 
		blank=True
		)
	telefone2 = models.CharField(
	    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
		#validators=[phone_regex], 
		max_length=17, 
		blank=True
		)
	email = models.EmailField(
		max_length=70, 
		blank=True		
		)
	descricao = models.CharField(
		max_length=150,
		blank=True			
		)
	imagem = models.FileField( 
		upload_to='empresas_servicos', 
		blank=True,
		)

	def __str__(self):
		return 'Empresa: {}, Contato: {} '.format(self.nome, self.contato)