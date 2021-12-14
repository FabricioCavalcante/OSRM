from django.contrib import admin
from users.models import User

class Listando_Requisicoes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'placa_patrimonio')

# Register your models here.
admin.site.register(User)