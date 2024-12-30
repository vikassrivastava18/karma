from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Karma
from .serializers import KarmaSerializer


class KarmaListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer


class KarmaDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Karma.objects.all()
    serializer_class = KarmaSerializer
    