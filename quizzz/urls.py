from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data,
    save_quiz
)

app_name='quizzz'

urlpatterns = [
    
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/data/', quiz_data, name='quiz-data'),
    path('<pk>/save/', save_quiz, name='save_quiz'),
]