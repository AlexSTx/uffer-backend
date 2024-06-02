from rest_framework import serializers
from base.models import Usuario, Motorista

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class MotoristaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Motorista
        fields = '__all__'