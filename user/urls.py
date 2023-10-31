from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.register, name='register'),
    path('entrar/', views.login, name='login')
]