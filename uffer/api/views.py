from base.models import Usuario, Motorista
from .serializers import UsuarioSerializer, MotoristaSerializer

from rest_framework import generics

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDetail(generics.RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MotoristasList(generics.ListCreateAPIView):
    queryset = Motorista
    serializer_class = MotoristaSerializer


class MotoristaDetails(generics.RetrieveDestroyAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer