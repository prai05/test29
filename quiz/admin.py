from django.contrib import admin
from .models import Question, Choice

# # Register your models here.

admin.site.site_title = 'Quiz'
admin.site.site_header = 'Quiz Administration'

# can Add Choice in each Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
