from django.db import models
from django.core.validators import validate_email, validate_slug

# Create your models here.

class Usuario (models.Model):
    nome = models.CharField(max_length=256, validators=[validate_slug])
    email = models.CharField(max_length=320, validators=[validate_email])
    created = models.DateTimeField(auto_now_add=True)

class Motorista(models.Model):
    cnh = models.BigIntegerField(unique=True)
    usuario_id = models.OneToOneField(to=Usuario)