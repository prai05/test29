from django.urls import path

from . import views

# Namespacing URL names {% url 'quiz:question'%}
app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('results/', views.results, name='results'),
]
