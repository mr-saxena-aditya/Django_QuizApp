import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from .models import Question, QuizResult  # Importing models
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# View to list all available questions
def question_list(request):
    questions = Question.objects.all()  # Fetch all questions from the database
    return render(request, 'question_list.html', {'questions': questions})

# View to start the quiz (5 random questions)
@login_required(login_url='/login/')  # Requires user authentication
def quiz(request):
    questions = Question.objects.all()  # Fetch all questions from the database
    random_questions = random.sample(list(questions), 5)  # Select 5 random questions
    return render(request, 'quiz.html', {'questions': random_questions})

# View to display quiz results
@login_required(login_url='/login/')  # Requires user authentication
def quiz_result(request):
    if request.method == 'POST':
        user_score = 0
        question_results = []

        selected_question_ids = [int(key.split('_')[1]) for key in request.POST if key.startswith('question_')]
        questions = Question.objects.filter(id__in=selected_question_ids)

        # Evaluate user answers and gather question results
        for question in questions:
            selected_choice_id = int(request.POST.get('question_' + str(question.id)))
            user_choice = question.get_choice_by_id(selected_choice_id)
            correct_choice = question.get_choice_by_id(question.correct_choice)

            if selected_choice_id == question.correct_choice:
                user_score += 1

            question_results.append({
                'question_text': question.question_text,
                'user_choice': user_choice,
                'correct_choice': correct_choice,
            })

        # Create and save a new QuizResult object
        quiz_result = QuizResult(user=request.user, score=user_score, timestamp=timezone.now())
        quiz_result.save()

        return render(request, 'quiz_result.html', {'user_score': user_score, 'question_results': question_results})
    else:
        # Fetch 5 random questions from the database
        random_questions = random.sample(list(Question.objects.all()), 5)
        return render(request, 'quiz_result.html', {'random_questions': random_questions})

# View for the homepage
def homepage(request):
    return render(request, 'homepage.html')

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Custom login view
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Log in the user
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# View to handle user logout
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('homepage')  # Redirect to the homepage after logging out
