from django.db import models
from condominio.models import Apartamento


class Visitante(models.Model):
    nome = models.CharField(max_length=200)
    documento = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Visita(models.Model):

    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)

    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField(null=True, blank=True)


class Encomenda(models.Model):

    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)

    descricao = models.CharField(max_length=255)
    data_recebimento = models.DateTimeField(auto_now_add=True)

    recebido_por = models.CharField(max_length=100)

    entregue = models.BooleanField(default=False)
    data_entrega = models.DateTimeField(null=True, blank=True)