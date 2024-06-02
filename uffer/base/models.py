from django.db import models
from django.core.validators import validate_email, validate_slug


# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=256, validators=[validate_slug])
    email = models.CharField(max_length=320, validators=[validate_email])
    created = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField


class Motorista(models.Model):
    cnh = models.BigIntegerField(unique=True)
    usuario_id = models.OneToOneField(to=Usuario, on_delete=models.DO_NOTHING)


class Veiculo(models.Model):
    placa = models.CharField(max_length=8, unique=True)
    cor = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    ano = models.IntegerField()
    marca = models.CharField(max_length=256)
    motorista_id = models.ForeignKey(to=Motorista, on_delete=models.CASCADE)


class Favorito(models.Model):
    nome = models.CharField(max_length=256)
    veiculo_id = models.ForeignKey(to=Veiculo, related_name="favoritos", on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(to=Usuario, related_name="favoritos", on_delete=models.CASCADE)

