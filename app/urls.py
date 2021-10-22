from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view()),
    path('create/quiz/', QuizCreateView.as_view()),
    path('create/question/', QuestionCreateView.as_view()),
    path('delete/quiz/<int:pk>/', QuizDeleteView.as_view()),
    path('delete/question/<int:pk>/', QuestionDeleteView.as_view()),
    path('edit/question/<int:pk>/', QuestionEditView.as_view()),
    path('edit/quiz/<int:pk>/', QuizEditView.as_view()),
    path('register/', RegisterView.as_view()),
    path('all/quiz/', GetQuizView.as_view()),
    path('quiz/view/<int:pk>/', GetQuestionView.as_view()),
    path('answer/create/', CreateAnswer.as_view()),
    path('answer/view/', GetAnswerList.as_view()),

]