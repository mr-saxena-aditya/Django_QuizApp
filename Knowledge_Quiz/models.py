from django.db import models
from django.contrib.auth.models import User

# Model representing a question in the quiz
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    
    # Using PositiveIntegerField with choices to represent the correct choice
    correct_choice = models.PositiveIntegerField(choices=[
        (1, 'Choice 1'),
        (2, 'Choice 2'),
        (3, 'Choice 3'),
        (4, 'Choice 4')
    ])
    
    def __str__(self):
        return self.question_text

    # Mapping between choice IDs and their corresponding field names
    CHOICES = {
        1: 'choice1',
        2: 'choice2',
        3: 'choice3',
        4: 'choice4'
    }

    # Method to get the text of a choice by its ID
    def get_choice_by_id(self, choice_id):
        choice_field_name = self.CHOICES.get(choice_id)
        if choice_field_name:
            return getattr(self, choice_field_name)
        return None

# Model representing a quiz result for a user
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"
