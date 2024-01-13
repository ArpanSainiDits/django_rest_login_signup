# accounts/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)       
        return super(CustomUserSerializer, self).create(validated_data) 
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        # extra_kwargs = {'password': {'write_only': True}}



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
