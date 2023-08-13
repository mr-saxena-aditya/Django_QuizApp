import random
from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def quiz(request):
    questions = Question.objects.all()
    random_questions = random.sample(list(questions), 5)
    return render(request, 'quiz.html', {'questions': random_questions})
from django.shortcuts import render
from random import sample
from .models import Question

def quiz_result(request):
    if request.method == 'POST':
        user_score = 0
        question_results = []

        selected_question_ids = [int(key.split('_')[1]) for key in request.POST if key.startswith('question_')]
        questions = Question.objects.filter(id__in=selected_question_ids)

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

        return render(request, 'quiz_result.html', {'user_score': user_score, 'question_results': question_results})
    else:
        # Fetch 5 random questions from the database
        random_questions = sample(list(Question.objects.all()), 5)
        return render(request, 'quiz_result.html', {'random_questions': random_questions})
