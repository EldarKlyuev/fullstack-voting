# polls/views.py

from rest_framework import generics
from .models import Poll
from .serializer import PollSerializer

class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
