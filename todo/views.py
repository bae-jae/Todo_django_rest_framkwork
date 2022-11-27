from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer
from todo import serializers

class TodoAPI(APIView):

    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        print(serializer.data)
        return Response(serializer.data, status.HTTP_200_OK)


class TodoDetailAPI(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False, important=True)
        serializer = TodoDetailSerializer(todos, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
