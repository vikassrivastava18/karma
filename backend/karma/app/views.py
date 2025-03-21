from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response

from .models import Karma, Todo, Reflection
from .serializers import KarmaSerializer, ReflectionSerializer, TodoSerializer

# Get today's date
today = timezone.now().date() + timedelta(days=1)


class HomeView(generics.GenericAPIView):
    """
        GET - Returns a welcome message
    """
    def get(self, request):
        return render(request, 'index.html')


class KarmaListView(generics.ListCreateAPIView):
    """
        GET - Returns a list of all karmas
        POST - Creates a new Karma
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer

    def get(self, request):
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


class ReflectionView(generics.ListCreateAPIView):
    """
        GET - Returns a list of all reflections
        POST - Creates a new reflection
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer

    def get(self, request, *args, **kwargs):
        karmas = Reflection.objects.filter(date=today)
        serializer = ReflectionSerializer(karmas, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ReflectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    