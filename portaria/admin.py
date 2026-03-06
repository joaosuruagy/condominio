from django.contrib import admin
from .models import Visitante, Visita, Encomenda

class EncomendaAdmin(admin.ModelAdmin):
    list_display = ("apartamento", "descricao", "entregue", "data_recebimento")
    list_filter = ("entregue",)
    search_fields = ("descricao",)

class VisitaAdmin(admin.ModelAdmin):
    list_display = ("visitante", "apartamento", "data_entrada", "data_saida")
    list_filter = ("apartamento",)
    search_fields = ("visitante__nome",)

admin.site.register(Visitante)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(Encomenda, EncomendaAdmin)