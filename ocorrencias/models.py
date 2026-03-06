from django.db import models
from condominio.models import Apartamento


class Ocorrencia(models.Model):

    TIPO_OCORRENCIA = [
        ('advertencia', 'Advertência'),
        ('multa', 'Multa'),
    ]

    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=20, choices=TIPO_OCORRENCIA)

    descricao = models.TextField()

    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.apartamento}"