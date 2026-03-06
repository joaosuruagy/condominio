from django.contrib import admin
from .models import Pessoa, Veiculo, Pet


class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "telefone")
    search_fields = ("nome", "cpf")
    
class VeiculoInline(admin.TabularInline):
    model = Veiculo
    extra = 0


class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "telefone")
    search_fields = ("nome", "cpf")
    inlines = [VeiculoInline]


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Veiculo)
admin.site.register(Pet)

