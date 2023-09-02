from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import KeywordFreq
from .serializers import KeywordFreqSerializer

# Create your views here.


class KeywordFreqList(generics.ListAPIView):
    queryset = KeywordFreq.objects.all()
    serializer_class = KeywordFreqSerializer

class InsertVoteElemnt(APIView):
    def post(self, request):
        # user_id = request.data['user_id']

        # print(request)
        print(request.data['text'])
        return Response("hi")