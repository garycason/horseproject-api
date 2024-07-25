from rest_framework import serializers
from horseapi.models import Horse, FavoriteHorse
from django.contrib.auth.models import User

class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = '__all__'

class FavoriteHorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteHorse
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
