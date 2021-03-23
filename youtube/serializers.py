from rest_framework import serializers
from youtube.models import Youtube


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = ['name', 'url', 'image', 'categori']


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['user_id', 'user_passward']
