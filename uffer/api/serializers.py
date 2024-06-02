from rest_framework import serializers
from base.models import Usuario, Motorista, Veiculo, Local, Favorito, LocalPadrao, Trajeto, Parada, Carona, Passageiro

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Motorista
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class LocalPadraoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalPadrao
        fields = '__all__'

class TrajetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajeto
        fields = '__all__'

class ParadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parada
        fields = '__all__'

class CaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carona
        fields = '__all__'

class PassageiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passageiro
        fields = '__all__'