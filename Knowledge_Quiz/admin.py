from django.contrib import admin
from .models import Question, QuizResult

# Customizing the Question model admin display
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_choice')

# Registering the Question model with its custom admin display
admin.site.register(Question, QuestionAdmin)

# Customizing the QuizResult model admin display
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    # Displayed fields in the list view of the admin page
    list_display = ('user', 'score', 'timestamp')

    # Adding filters to the right side of the admin page for easy data filtering
    list_filter = ('user',)

    # Adding a search field to allow searching by user's username
    search_fields = ('user__username',)

    # You can further customize other options and behaviors here as needed
    # For example, you can add date_hierarchy, ordering, readonly_fields, etc.
    # More options: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

# Note: Make sure to customize other options and behaviors as per your project requirements
