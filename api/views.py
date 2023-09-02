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
            "text": "Would you like to play a game?",
            "attachments": [
                {
                    "text": "Choose a game to play",
                    "fallback": "You are unable to choose a game",
                    "callback_id": "wopr_game",
                    "color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "game",
                            "text": "Chess",
                            "type": "button",
                            "value": "chess"
                        },
                        {
                            "name": "game",
                            "text": "Falken's Maze",
                            "type": "button",
                            "value": "maze"
                        },
                        {
                            "name": "game",
                            "text": "Thermonuclear War",
                            "style": "danger",
                            "type": "button",
                            "value": "war",
                            "confirm": {
                                "title": "Are you sure?",
                                "text": "Wouldn't you prefer a good game of chess?",
                                "ok_text": "Yes",
                                "dismiss_text": "No"
                            }
                        }
                    ]
                }
            ]
        }
        

        return Response(res)
        # return Response(f"{user_nick} 님의 관심 키워드는 {keywords} 입니다")