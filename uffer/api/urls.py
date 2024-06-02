from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UsuariosList.as_view()),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view()),

    path('motoristas/', views.MotoristasList.as_view()),
    path('motoristas/<int:pk>/', views.MotoristaDetail.as_view()),

    path('veiculos/', views.VeiculosList.as_view()),
    path('veiculos/<int:pk>/', views.VeiculoDetail.as_view()),

    path('locais/', views.LocaisList.as_view()),
    path('locais/<int:pk>/', views.LocalDetail.as_view()),

    path('favoritos/', views.FavoritosList.as_view()),
    path('favoritos/<int:pk>/', views.FavoritoDetail.as_view()),

    path('locais_padrao/', views.LocaisPadraoList.as_view()),
    path('locais_padrao/<int:pk>/', views.LocalPadraoDetail.as_view()),

    path('trajetos/', views.TrajetosList.as_view()),
    path('trajetos/<int:pk>/', views.TrajetoDetail.as_view()),

    path('paradas/', views.ParadasList.as_view()),
    path('paradas/<int:pk>/', views.ParadaDetail.as_view()),
    
    path('caronas/', views.CaronasList.as_view()),
    path('caronas/<int:pk>/', views.CaronaDetail.as_view()),

    path('passageiros/', views.PassageirosList.as_view()),
    path('passageiros/<int:pk>/', views.PassageiroDetail.as_view()),
]