from base.models import Usuario, Motorista, Veiculo, Local, Favorito, LocalPadrao, Trajeto, Parada, Carona, Passageiro
from .serializers import UsuarioSerializer, MotoristaSerializer, VeiculoSerializer, LocalSerializer, FavoritoSerializer, LocalPadraoSerializer, TrajetoSerializer, ParadaSerializer, CaronaSerializer, PassageiroSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.schemas import AutoSchema


class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDetail(generics.RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MotoristasList(generics.ListCreateAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer


class MotoristaDetail(generics.RetrieveDestroyAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer


class VeiculosList(generics.ListCreateAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class VeiculoDetail(generics.RetrieveDestroyAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class LocaisList(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class LocalDetail(generics.RetrieveDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class FavoritosList(generics.ListCreateAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class FavoritoDetail(generics.RetrieveDestroyAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class LocaisPadraoList(generics.ListCreateAPIView):
    queryset = LocalPadrao.objects.all()
    serializer_class = LocalPadraoSerializer


class LocalPadraoDetail(generics.RetrieveDestroyAPIView):
    queryset = LocalPadrao.objects.all()
    serializer_class = LocalPadraoSerializer


class TrajetosList(generics.ListCreateAPIView):
    queryset = Trajeto.objects.all().prefetch_related()
    serializer_class = TrajetoSerializer


class TrajetoDetail(generics.RetrieveDestroyAPIView):
    queryset = Trajeto.objects.all()
    serializer_class = TrajetoSerializer


class ParadasList(generics.ListCreateAPIView):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer


class ParadaDetail(generics.RetrieveDestroyAPIView):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer


class CaronasList(generics.ListCreateAPIView):
    queryset = Carona.objects.all()
    serializer_class = CaronaSerializer


class CaronaDetail(generics.RetrieveDestroyAPIView):
    queryset = Carona.objects.all()
    serializer_class = CaronaSerializer


class PassageirosList(generics.ListCreateAPIView):
    queryset = Passageiro.objects.all()
    serializer_class = PassageiroSerializer


class PassageiroDetail(generics.RetrieveDestroyAPIView):
    queryset = Passageiro.objects.all()
    serializer_class = PassageiroSerializer