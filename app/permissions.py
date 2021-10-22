from rest_framework import permissions
from .models import *
from datetime import datetime
class IsTimeNotDefined(permissions.BasePermission) :
    def has_permission(self, request, view):
        #request.data
        quiz_set = Quiz.objects.filter(id = request.data['quiz_id'])
        for quiz in quiz_set :

            if quiz.start.year != datetime(1024, 10,10).year :
                return False
        return True