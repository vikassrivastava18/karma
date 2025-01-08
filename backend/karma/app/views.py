from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response

from .models import Karma, Todo
from .serializers import KarmaSerializer, TodoSerializer

# Get today's date
today = timezone.now().date()


class KarmaListView(generics.ListCreateAPIView):
    """
        GET - Returns a list of all karmas
        POST - Creates a new Karma
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer

    def get(self, request, *args, **kwargs):
        karmas = Karma.objects.filter(date=today)
        serializer = KarmaSerializer(karmas, many=True)
        return Response(serializer.data)

class KarmaDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer


class ToDoListView(generics.ListCreateAPIView):
    """
        GET - Returns list of todos
        POST - Creates a new Todo
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    

class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        GET - Returns a single Karma
        PUT - Updates a single Karma
        DELETE - Deletes a single Karma
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    