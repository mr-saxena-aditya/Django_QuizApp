from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choice')

admin.site.register(Question, QuestionAdmin)
