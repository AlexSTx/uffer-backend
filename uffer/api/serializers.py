from rest_framework import serializers
from base.models import Usuario, Motorista, Veiculo, Local, Favorito, LocalPadrao, Trajeto, Parada, Carona, Passageiro, SolicitacaoCarona
from django.contrib.auth.models import User
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

class ParadaStandaloneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parada
        fields = ['id', 'trajeto', 'posicao', 'local']

class ParadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parada
        fields = ['id', 'posicao', 'local']

class TrajetoSerializer(serializers.ModelSerializer):
    paradas = ParadaSerializer(many = True)
    class Meta:
        model = Trajeto
        fields = ['id', 'origem', 'destino', 'paradas']
    
    def create(self, validated_data):
        paradas_data = validated_data.pop('paradas')
        trajeto = Trajeto.objects.create(**validated_data)
        for parada_data in paradas_data:
            Parada.objects.create(trajeto = trajeto, **parada_data)
            print(trajeto)
        return trajeto

class CaronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carona
        fields = '__all__'


class PassageiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passageiro
        fields = '__all__'

class SolicitacaoCaronaSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = SolicitacaoCarona
        fields = ['data_hora_chegada', 'quantidade_passageiros', 'em_aberto', 'passa_por', 'usuario']


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']