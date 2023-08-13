from django.contrib import admin
from .models import Question, QuizResult

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choice')

admin.site.register(Question, QuestionAdmin)

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'timestamp')  # Customize the fields to be displayed in the list view
    list_filter = ('user',)  # Add filters to the right side of the admin page
    search_fields = ('user__username',)  # Add a search field for the user's username

    # You can customize other options and behaviors here as needed
