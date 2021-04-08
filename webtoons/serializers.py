from rest_framework import serializers
from webtoons.models import Daum
from webtoons.models import Naver


class DaumSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Daum
        fields = ['name', 'url', 'image','category']

class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Naver
        fields = ['name', 'url', 'image','category']

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['user_id', 'user_passward']