from django.db import models

# Create your models here.
from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    apartamento = models.ForeignKey(
        'condominio.Apartamento',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.placa


class Pet(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    raca = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome