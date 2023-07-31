from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer 
from rest_framework.generics import ListCreateAPIView
from django.urls import reverse_lazy


class TodoCreateListAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

