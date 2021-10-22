from nltk import pk
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import  *
import string
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import random
class MyTokenObtainPairSerializer(TokenObtainPairSerializer) :

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class QuizCreateSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Quiz
        fields = ('title', 'description')
class QuestionEditSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields = ('text', )
class QuestionCreateSerializer(serializers.ModelSerializer) :
    question_type = serializers.CharField(required=True)

    quiz_id = serializers.CharField(required=True)
    class Meta :
        model = Question
        fields = '__all__'

class QuizListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Quiz
        fields = '__all__'

class QuestionListSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question
        fields  = '__all__'
class AnswerQuestionSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Answer
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer) :


    password = serializers.CharField(required=False)
    username = serializers.CharField(required=False)


    class Meta:
        model = User
        fields = ('username', 'password')


    def create(self, validated_data):
        id = str(random.randint(100000, 1000000))
        #upass = ''.join(random.choice(string.ascii_letters + string.digits + '!@#$%^&*()_') for _ in range(10))
        user = User.objects.create_user(username=id, password=id)
        #print(uname, upass)

        return user

