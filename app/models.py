from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tarefa(models.Model):
    PRIORIDADES = (
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baixa'),
    )
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=120)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES)
    usuario = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
