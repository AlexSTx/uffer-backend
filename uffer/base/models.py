from django.db import models
from django.core.validators import validate_email, validate_slug


# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=256, validators=[validate_slug])
    email = models.CharField(max_length=320, validators=[validate_email])
    created = models.DateTimeField(auto_now_add=True)
    # TODO: implementar foto, é mais complicado que só deixar aqui
    # foto = models.ImageField()


class Motorista(models.Model):
    cnh = models.BigIntegerField(unique=True)
    usuario_id = models.OneToOneField(to=Usuario, on_delete=models.CASCADE)


class Veiculo(models.Model):
    placa = models.CharField(max_length=8, unique=True)
    cor = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    ano = models.IntegerField()
    marca = models.CharField(max_length=256)
    motorista_id = models.ForeignKey(to=Motorista, on_delete=models.CASCADE)


class Local(models.Model):
    coordenadas = models.CharField(max_length=256)


class Favorito(models.Model):
    nome = models.CharField(max_length=256)
    local_id = models.ForeignKey(to=Local, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)


class LocalPadrao(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    local_id = models.ForeignKey(to=Local, on_delete=models.CASCADE)


class Trajeto(models.Model):
    origem_id = models.ForeignKey(to=Local, related_name='origens', on_delete=models.CASCADE)
    destino_id = models.ForeignKey(to=Local, related_name='destinos', on_delete=models.CASCADE)

class Parada(models.Model):
    posicao = models.SmallIntegerField()
    trajeto_id = models.ForeignKey(to=Trajeto, on_delete=models.CASCADE)
    local_id = models.ForeignKey(to=Local, on_delete=models.CASCADE)

class Carona(models.Model):
    data_hora_chegada = models.DateTimeField()
    data_hora_saida = models.DateTimeField()
    assentos_disponveis = models.IntegerField(default=1)
    em_aberto = models.BooleanField(default=True)
    retorno = models.BooleanField(default=False)
    apenas_solicitacao = models.BooleanField(default=False)
    detalhes_adicionais = models.TextField(max_length=512)
    motorista_id = models.ForeignKey(to=Motorista, null=True, on_delete=models.SET_NULL)
    trajeto_id = models.ForeignKey(to=Trajeto, null=True, on_delete=models.SET_NULL)


class Passageiro(models.Model):
    carona_id = models.ForeignKey(to=Carona, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
