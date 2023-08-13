from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    correct_choice = models.PositiveIntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')])

    def __str__(self):
        return self.question_text
    
    CHOICES = {
        1: 'choice1',
        2: 'choice2',
        3: 'choice3',
        4: 'choice4'
    }

    def get_choice_by_id(self, choice_id):
        choice_field_name = self.CHOICES.get(choice_id)
        if choice_field_name:
            return getattr(self, choice_field_name)
        return None
