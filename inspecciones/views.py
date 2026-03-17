

# views.py
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario



from  .serializer import LoginSerializer

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = LoginSerializer

    
class ValidatePasswordView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = LoginSerializer

    def get(self, request, nombre, clave):
        try:
            usuario = Usuario.objects.get(nombre=i801_nombre)
            return Response(LoginSerializer(usuario).data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado o clave incorrecto"}, status=status.HTTP_404_NOT_FOUND)

