from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from rest_framework import generics, viewsets
from .models import *
from django.contrib.auth.models import User

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class QuizCreateView(generics.CreateAPIView) :
    queryset = Quiz.objects.all()
    serializer_class = QuizCreateSerializer
    permission_classes = (IsAdminUser, )

class QuestionCreateView(generics.CreateAPIView) :
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer
    permission_classes = (IsAdminUser, )

class QuizDeleteView(generics.DestroyAPIView) :
    queryset = Quiz.objects.all()
    serializer_class = QuizCreateSerializer
    permission_classes = (IsAdminUser, )

class QuestionDeleteView(generics.DestroyAPIView) :
    queryset = Question.objects.all()
    serializer_class = QuestionEditSerializer
    permission_classes = (IsAdminUser, )
class QuestionEditView(generics.UpdateAPIView) :
    queryset = Question.objects.all()
    serializer_class = QuestionEditSerializer
    permission_classes = (IsAdminUser, )
class QuizEditView(generics.UpdateAPIView) :
    queryset = Quiz.objects.all()
    serializer_class = QuizCreateSerializer
    permission_classes = (IsAdminUser, )

class RegisterView(generics.CreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class GetQuizView(generics.ListAPIView) :
    queryset = Quiz.objects.all()
    serializer_class = QuizListSerializer
class GetQuestionView(generics.ListAPIView) :

    serializer_class = QuestionListSerializer
    def get_queryset(self):
        id = self.kwargs['pk']
        return Question.objects.filter(quiz_id = id)
class CreateAnswer(generics.CreateAPIView) :

    serializer_class = AnswerQuestionSerializer
    queryset = Answer.objects.all()

class GetAnswerList(generics.ListAPIView) :
    serializer_class =  AnswerQuestionSerializer
    def get_queryset(self):
        id = self.request.user.id
        print(id)
        return Answer.objects.filter(user_id = id)
