from django.urls import path
from .views import PollListCreateView

urlpatterns = [
    path('polls/', PollListCreateView.as_view(), name='poll-list-create'),
]
