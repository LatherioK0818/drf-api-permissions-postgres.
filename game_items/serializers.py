from rest_framework import serializers
from .models import GameItem

class GameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameItem
        fields = '__all__'