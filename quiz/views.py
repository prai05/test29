from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Choice, Question
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def question(request):
    question_text = Question.objects.all()
    context = {
        'question_text': question_text,
    }
    return render(request, 'question.html', context)

def results(request):
    if request.method =='POST':
        question_text = Question.objects.all()
        question_num = len(question_text)
        choice = Choice.objects.all()
        point = 0

        # check point between choice and selected
        for i in range(question_num):
            if str(choice[i].corrected) == request.POST.get('choice'+str(i+1)):
                point += 1
        context = {
            'point': point,
            'question_num': question_num,
        }
        return render(request, 'results.html', context)
