from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserConfirmation

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ['id', 'username', 'password']
      extra_kwargs = {'password': {'write_only': True}}

class UserConfirmationSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserConfirmation
    fields = ['code']


class AuthorizeValidateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
