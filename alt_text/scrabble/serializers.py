from rest_framework import serializers
from .models import Scrabble

class ScrabbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrabble
        fields = '__all__'