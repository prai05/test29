from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Choice, Question
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    return render(request, 'index.html')

def question(request):
    #question_text = Question.objects.order_by('-pub_date')[:5]
    question_text = Question.objects.all()
    context = {
        'question_text': question_text,
    }
    return render(request, 'question.html', context)

def results(request):
    if request.method =='POST':
        question_text = Question.objects.all() #.order_by('-id')
        question_num = len(question_text)
        point = 0
        choice1 = Choice.objects.get(pk=1)
        choice2 = Choice.objects.get(pk=2)
        choice3 = Choice.objects.get(pk=3)
        radio1 = request.POST.get('choice1')
        radio2 = request.POST.get('choice2')
        radio3 = request.POST.get('choice3')
        for i in range(question_num):
            if str(Choice.objects.get(pk=i+1).corrected) == request.POST.get('choice' + str(i+1)):
                point += 1
        context = {
            'point': point,
            'question_num': question_num,
            'question_text': question_text,
            'choice1': choice1,
            'choice2': choice2,
            'choice3': choice3,
            'radio1': radio1,
            'radio2': radio2,
            'radio3': radio3,
        }
        return render(request, 'results.html', context)
