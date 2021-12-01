from django.contrib import admin
from .models import InserirDados

class Listando_Requisicoes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'placa_patrimonio')

# Register your models here.
admin.site.register(InserirDados, Listando_Requisicoes)