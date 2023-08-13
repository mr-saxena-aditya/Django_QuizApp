from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.question_list, name='question_list'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_result/', views.quiz_result, name='quiz_result'),  # Define this URL pattern
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),  # Replace 'register' with your actual registration view
    path('login/', views.custom_login, name='login'),  # Replace 'login' with your actual login view
    path('logout/', views.logout_view, name='logout'),  # Add the URL pattern for the logout view
]