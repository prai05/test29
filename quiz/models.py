import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question_text

BOOL_CHOICES = ((True, 'True'), (False, 'False'))

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    corrected = models.BooleanField(choices=BOOL_CHOICES)
    def __boo__(self):
        return self.corrected
