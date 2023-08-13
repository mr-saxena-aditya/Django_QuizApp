from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.question_list, name='question_list'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_result/', views.quiz_result, name='quiz_result'),  # Define this URL pattern
]