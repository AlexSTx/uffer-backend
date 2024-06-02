from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UsuariosList.as_view()),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view())
]