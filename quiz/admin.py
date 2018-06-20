from django.contrib import admin
from .models import Question, Choice

# # Register your models here.

admin.site.site_title = 'Quiz'
admin.site.site_header = 'Quiz Administration'

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['created', 'question_text']

class ChoiceInline(admin.StackedInline):
    model = Choice
    # radio_fields = {"Choice": admin.VERTICAL}
    # radio_fields = {"group": admin.VERTICAL}
    # widgets = {
    #         'corrected': corrected.RadioSelect
    #     }
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [ChoiceInline]
    # radio_fields = {"quiz": admin.VERTICAL}

admin.site.register(Question, QuestionAdmin)
