import datetime
from django.db import models
from django.utils import timezone

# keep question_text in database
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

BOOL_CHOICES = ((True, 'True'), (False, 'False'))
# keep corrected in database
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    corrected = models.BooleanField(choices=BOOL_CHOICES)
