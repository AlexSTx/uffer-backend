from base.models import Usuario
from .serializers import UsuarioSerializer

from rest_framework import generics

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDetail(generics.RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer