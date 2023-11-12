from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('verificar_login/', views.verificar_login, name='verificar_login'),
    path('calculo/', views.calculo, name='calculo'),
    path('resultado/', views.resultado, name='resultado'),
]
