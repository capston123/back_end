from rest_framework import serializers
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_passward', 'user_email']

class UsersAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['user_id', 'user_passward']