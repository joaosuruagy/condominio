from django.db import models
from pessoas.models import Pessoa


class Bloco(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Apartamento(models.Model):
    numero = models.CharField(max_length=10)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bloco} - {self.numero}"


class Ocupacao(models.Model):

    TIPO_OCUPACAO = [
        ('proprietario', 'Proprietário'),
        ('inquilino', 'Inquilino'),
        ('morador', 'Morador'),
    ]

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=20, choices=TIPO_OCUPACAO)

    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pessoa} - {self.apartamento} ({self.tipo})"