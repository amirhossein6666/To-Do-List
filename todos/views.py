from .models import Todo
from .serializers import TodoSerializer 
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])  # We're using GET here to retrieve the list of todos
@permission_classes([IsAuthenticated])
def todo_list_view(request):
    todos= Todo.objects.filter(author=request.user)
    serializer = TodoSerializer(todos, many= True)
    return Response (serializer.data)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def TodoCreate(request):
    if request.method == 'POST':
        data = {
            'title': request.data['title'],
            'description': request.data['description'],
            'author': request.user.id # Use the user instance to set the author field
        }
        serialized_Todo = TodoSerializer(data=data)
        if serialized_Todo.is_valid():
            serialized_Todo.save()
            return Response (serialized_Todo.data, status=status.HTTP_201_CREATED)
        return Response(serialized_Todo.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=404)
        
    data = {
        'title': request.data['title'],
        'description': request.data['description'],
        'is_finished' : request.data['is_finished'],
        'author': request.user.id # Use the user instance to set the author field
    } 
    serializer = TodoSerializer(todo, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=400)