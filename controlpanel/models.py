from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    nome     = models.CharField(max_length=56)
    cpf      = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email    = models.CharField(max_length=256)
    endereco = models.OneToOneField('Endereco', on_delete=models.CASCADE)

class Endereco(models.Model):
    clienteEndereco  = models.OneToOneField('Cliente', on_delete=models.CASCADE)
    cep      = models.CharField(max_length=8)
    clienteEndereco = models.CharField(max_length=512)
    bairro   = models.CharField(max_length=512)
    cidade   = models.CharField(max_length=512)
    numero   = models.IntegerField()
    UF = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

# Create your models here.
