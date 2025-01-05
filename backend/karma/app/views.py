

from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response

from .models import Karma, next_day_date, prev_day_date
from .serializers import KarmaSerializer

# Get today's date
today = timezone.now().date()


class KarmaListView(generics.ListCreateAPIView):
    """
        Returns a list of all karmas
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
    