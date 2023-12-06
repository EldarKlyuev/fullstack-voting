from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('choices/', ChoiceListCreateView.as_view(), name='choice-list-create'),
    path('votes/', VoteListCreateView.as_view(), name='vote-list-create'),
    path('vote/', VoteCreateAPIView.as_view()),
    path('card/', QuestionGetAPIView.as_view()),
    path('card/<int:pk>/', QuestionDeleteAPIView.as_view())
]
