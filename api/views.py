from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import KeywordFreq, VoteElement
from .serializers import KeywordFreqSerializer

# Create your views here.


class KeywordFreqList(generics.ListAPIView):
    queryset = KeywordFreq.objects.all()
    serializer_class = KeywordFreqSerializer

class InsertVoteElemnt(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        user_name = request.data['user_name']
        text = request.data['text']
        user_nick, keywords = text.split(':')
        user_nick = user_nick.strip()

        for keyword in keywords.split(','):
            VoteElement.objects.create(user_id=user_id, user_name=user_name, user_nick=user_nick, keyword=keyword.strip())

            keyFreq, _ = KeywordFreq.objects.get_or_create(keyword=keyword.strip())
            keyFreq.freq = keyFreq.freq + 1
            keyFreq.save()

        res = {
            "response_type": "in_channel",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{user_nick} 님의 관심 키워드는 {keywords} 입니다"
                    }
                },
                {
			        "type": "section",
			        "text": {
                                "type": "mrkdwn",
                                "text": "<https://naver.com|결과보기>"
			                }
		        }
            ]
        }
        

        return Response(res)
        # return Response(f"{user_nick} 님의 관심 키워드는 {keywords} 입니다")