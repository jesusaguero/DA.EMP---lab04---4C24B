from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('calculadora.urls')),
    path('verificar_login/', include('calculadora.urls')),
    path('resultado/', include('calculadora.urls')),
]
