from django.contrib import admin
from .models import Bloco, Apartamento, Ocupacao


class OcupacaoInline(admin.TabularInline):
    model = Ocupacao
    extra = 0


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ("numero", "bloco")
    list_filter = ("bloco",)
    inlines = [OcupacaoInline]


admin.site.register(Bloco)
admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(Ocupacao)