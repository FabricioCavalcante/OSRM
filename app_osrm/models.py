from django.db import models
import datetime
from django.contrib.auth.models import User

class InserirDados(models.Model):
    #nome = models.CharField(max_length=100)
    nome = models.ForeignKey(User,on_delete=models.CASCADE)
    placa_patrimonio = models.IntegerField(blank=True)
    local = models.CharField(max_length=100)
    problema = models.TextField(max_length=300)
    horarioInsercao = models.DateTimeField(default=datetime.datetime.now, blank=True)