from django.db import models
import random
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=100)

    question_type_list = [('1', 'ответ с выбором одного варианта'),
                          ('2', 'ответ с выбором одного варианта'),
                          ('3', 'ответ с выбором нескольких вариантов')]

    question_type = models.CharField(choices=question_type_list, max_length=100, default='1')

    quiz_id = models.IntegerField(default=1)

class Quiz(models.Model) :
    title = models.CharField(max_length=50)

    start = models.DateField(default="2021-10-10")
    end = models.DateField(default="2021-10-11")

    description = models.CharField(max_length=250)
class Answer(models.Model) :

    text = models.CharField(max_length=500)
    question_id = models.CharField(max_length=25)
    user_id = models.CharField(max_length=25, default=1)