from django.db import models

# Create your models here.
from notas.models import Projeto


class Faturado(models.Model):
    """
    Modelo representando pagamentos feitos, seja de funcionarios, serviços, materiais ou equipamentos.abs
    """
    vencimento = models.DateField()
    descricao = models.CharField(
        max_length=30,
        blank=True
        )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        )
    pago = models.BooleanField(
        default=False
		)
    #Fk Projetos.
    projeto = models.ForeignKey(
        Projeto, 
        on_delete=models.SET_NULL, 
        null=True
        )

    def __str__(self):
        return 'Vencimento: {}, Valor: {}'.format(self.vencimento, self.valor)
        
    class Meta:
        ordering = ["-vencimento"]