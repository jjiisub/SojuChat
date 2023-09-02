from django.db import models


class VoteElement(models.Model):
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_nick = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.user_nick} / {self.keyword}"

class KeywordFreq(models.Model):
    keyword = models.CharField(max_length=100)
    freq = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.keyword}-{self.freq}"