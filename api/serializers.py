from rest_framework import serializers
from .models import KeywordFreq, VoteElement

class KeywordFreqSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordFreq
        fields = '__all__'


class VoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteElement
        fields = '__all__'