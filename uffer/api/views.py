from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Usuario
from .serializers import UsuarioSerializer

@api_view(['GET'])
def getData(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUsuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)