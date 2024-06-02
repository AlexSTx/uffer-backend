from base.models import Usuario, Motorista, Veiculo, Local, Favorito, LocalPadrao, Trajeto, Parada, Carona, Passageiro
from .serializers import UsuarioSerializer, MotoristaSerializer, VeiculoSerializer, LocalSerializer, FavoritoSerializer, LocalPadraoSerializer, TrajetoSerializer, ParadaSerializer, CaronaSerializer, PassageiroSerializer


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


class MotoristaDetail(generics.RetrieveDestroyAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer


class VeiculosList(generics.ListCreateAPIView):
    queryset = Veiculo
    serializer_class = VeiculoSerializer


class VeiculoDetail(generics.RetrieveDestroyAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class LocaisList(generics.ListCreateAPIView):
    queryset = Local
    serializer_class = LocalSerializer


class LocalDetail(generics.RetrieveDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class FavoritosList(generics.ListCreateAPIView):
    queryset = Favorito
    serializer_class = FavoritoSerializer


class FavoritoDetail(generics.RetrieveDestroyAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer


class LocaisPadraosList(generics.ListCreateAPIView):
    queryset = LocalPadrao
    serializer_class = LocalPadraoSerializer


class LocalPadraoDetail(generics.RetrieveDestroyAPIView):
    queryset = LocalPadrao.objects.all()
    serializer_class = LocalPadraoSerializer


class TrajetosList(generics.ListCreateAPIView):
    queryset = Trajeto
    serializer_class = TrajetoSerializer


class TrajetoDetail(generics.RetrieveDestroyAPIView):
    queryset = Trajeto.objects.all()
    serializer_class = TrajetoSerializer


class ParadasList(generics.ListCreateAPIView):
    queryset = Parada
    serializer_class = ParadaSerializer


class ParadaDetail(generics.RetrieveDestroyAPIView):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer


class CaronasList(generics.ListCreateAPIView):
    queryset = Carona
    serializer_class = CaronaSerializer


class CaronaDetail(generics.RetrieveDestroyAPIView):
    queryset = Carona.objects.all()
    serializer_class = CaronaSerializer


class PassageirosList(generics.ListCreateAPIView):
    queryset = Passageiro
    serializer_class = PassageiroSerializer


class PassageiroDetail(generics.RetrieveDestroyAPIView):
    queryset = Passageiro.objects.all()
    serializer_class = PassageiroSerializer