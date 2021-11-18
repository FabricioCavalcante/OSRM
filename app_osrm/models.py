from django.db import models
import datetime

class InserirDados(models.Model):
    nome = models.CharField(max_length=100)
    placa_patrimonio = models.IntegerField()
    local = models.CharField(max_length=100)
    problema = models.TextField(max_length=300)
    horarioInsercao = models.DateTimeField(default=datetime.datetime.now, blank=True)