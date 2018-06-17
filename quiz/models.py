#import datetime
from django.db import models
#from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    corrected = models.BooleanField(default=False)
