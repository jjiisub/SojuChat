from rest_framework import serializers
from .models import KeywordFreq

class KeywordFreqSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordFreq
        fields = '__all__'