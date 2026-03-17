from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import  Usuario

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
  

  
