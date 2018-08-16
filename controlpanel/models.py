from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=56)
    telefone = models.CharField(max_length=11)


class Endereco(models.Model):
    cliente_id = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=512)
    cidade = models.CharField(max_length=512)
    numero = models.IntegerField()
    estado = models.CharField(max_length=256)
    pais = models.CharField(max_length=256)

# Create your models here.
