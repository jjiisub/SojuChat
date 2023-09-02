from django.contrib import admin
from .models import VoteElement, KeywordFreq

# Register your models here.

admin.site.register(VoteElement)
admin.site.register(KeywordFreq)