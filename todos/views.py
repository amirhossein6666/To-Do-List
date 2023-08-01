from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer 
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from django.urls import reverse_lazy


class TodoListAPIView(ListAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.filter(author = self.request.user)

class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'


