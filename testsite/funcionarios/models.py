from django.db import models

# Create your models here.

class Funcionario(models.Model):
	"""
	Modelo representando pagamentos feitos, seja de funcionarios, serviços, materiais ou equipamentos.abs
	"""
	nome = models.CharField(
		max_length=70
		)

	data_nascimento = models.DateField(
        null=True, 
		blank=True        
		)

	cpf = models.CharField(
		max_length=15,
		unique=True, 
		null=True, 
		blank=True
	)
		
	rg = models.CharField(
		max_length=12,
		)

	endereco = models.CharField(
		max_length=150,
		null=True, 
		blank=True
		)

	cidade = models.CharField(
		max_length=60,
		null=True, 
		blank=True        
		)
	
	estado = models.CharField(
		max_length = 20,
		null=True, 
		blank=True        
		)

	telefone = models.CharField(
		max_length=15,
		null=True, 
		blank=True        
		)

	telefone2 = models.CharField(
		max_length=15,
		null=True, 
		blank=True        
		)

	email = models.EmailField(
		null=True, 
		blank=True
		)

	ativo = models.BooleanField(
		'ativo', 
		default=True
		)

	imagem = models.FileField( 
		upload_to='notas_compras', 
		blank=True,
		)

	#fk ocupação com o cargo do funcionario	
	ocupacao = models.ForeignKey(
		'Ocupacao', 
        on_delete=models.SET_NULL, 
		null=True, 
		blank=True
		)

	#fk vale refeição
	vale_refeicao = models.ForeignKey(
		'ValeRefeicao', 
        on_delete=models.SET_NULL, 
		null=True, 
		blank=True
		)	

	#fk vale transporte
	vale_transporte = models.ForeignKey(
		'ValeTransporte', 
        on_delete=models.SET_NULL, 
		null=True, 
		blank=True
		)	

	#methods
	def __str__(self):
		return 'Nome: {}, RG: {}'.format(self.nome, self.rg)


class Ocupacao(models.Model):
	"""
	Modelo representando cargos possiveis dos funcionarios e seus respectivos salários.
	"""
	nome = models.CharField(
		max_length=30
		)

	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2, 
		null=True,        
		blank=True
		)

	#methods
	def __str__(self):
		return '{}, Valor: {}'.format(self.nome, self.valor)

class ValeRefeicao(models.Model):
	"""
	Modelo representando vale refeição e valores possiveis.
	"""
	nome = models.CharField(
		max_length=30
		)

	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2, 
		null=True,        
		blank=True
		)

	#methods
	def __str__(self):
		return 'Nome:{}, Valor: {}'.format(self.nome, self.valor)

class ValeTransporte(models.Model):
	"""
	Modelo representando vale refeição e valores possiveis.
	"""
	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2, 
		null=True,        
		blank=True
		)

	#methods
	def __str__(self):
		return '{}'.format(self.valor)

class Pagamento(models.Model):
	data = models.DateField(
		blank=False
		)

	valor = models.DecimalField(
		max_digits=10, 
		decimal_places=2, 
		
		)
	
	tipo = models.CharField(
		max_length=30,
		null=True
		)
	
	comentario = models.CharField(
		max_length=60,
		null=True, 
		blank=True        
		)


	#methods
	def __str__(self):
		return '<Tipo: {}, Data: {}, Valor: {}>'.format(self.tipo, self.data, self.valor)
