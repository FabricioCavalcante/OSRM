from django.db import models

# Create your models here.
class criar_tecnico(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)