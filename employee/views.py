from django.shortcuts import render
from rest_framework import generics

from employee.models import User


# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
