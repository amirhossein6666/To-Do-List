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
        print(request.data)
        request.data['author'] = request.user
        serialized_Todo = TodoSerializer(data=request.data)
        print("finish")
        print(serialized_Todo)
        if serialized_Todo.is_valid():
            serialized_Todo.save()
            return Response (serialized_Todo.data, status=status.HTTP_201_CREATED)
        return Response(serialized_Todo.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'