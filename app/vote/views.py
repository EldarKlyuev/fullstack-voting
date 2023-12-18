from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import *
from .serializer import *

class RegisterView(APIView):
    '''Вью регистрации пользователя'''

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_instance = User.objects.get(username=serializer.validated_data['username'])
            token, created = Token.objects.get_or_create(user=user_instance)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    '''Вью логина пользователя'''

    def post(self, request, *args, **kwargs):
        try:
            user_instance = User.objects.get(username=request.data['username'])
            token = Token.objects.get(user=user_instance)
        except Exception as ex:
            print(ex)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
        

class CheckRoleUserAPIView(APIView):
    '''Проверка роли пользователя'''

    def post(self, request):
        try:
            token = Token.objects.get(key=request.data.get('token'))
            user = User.objects.get(pk=token.user_id)

        except Exception as ex:
            print(ex)

        return Response({"role": str(user.role_sys)}, status=status.HTTP_200_OK)

class DeleteTokenAPIView(APIView):
    '''Выход пользователя из системы'''

    def delete(self, request):
        try:
            token = Token.objects.get(key=request.data.get('token'))
            token.delete()
        except Exception as ex:
            print(ex)

        return Response(status=status.HTTP_204_NO_CONTENT)

class QuestionListCreateView(generics.ListCreateAPIView):
    '''Вью создания вопроса'''

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        question_text = request.data['questionText']
        selected_choices = request.data['selectedChoices']

        # Create the question and associated choices
        question = Question.objects.create(question_text=question_text)
        for choice_text in selected_choices:
            Choice.objects.create(choice_text=choice_text, question=question)

        serializer = self.get_serializer(question)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class ChoiceListCreateView(generics.ListCreateAPIView):
    '''Вью создания выбора'''

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def list(self, request, *args, **kwargs):
        question_id = request.query_params['question_id']
        if question_id:
            choices = Choice.objects.filter(question_id=question_id)
            serializer = self.get_serializer(choices, many=True)
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)


class QuestionGetAPIView(APIView):
    '''Получение вопросов'''

    def get(self, request):
        question = Question.objects.all()
        choise = Choice.objects.all()
        serializer_question = QuestionSerializer(question, many=True)
        serializer_choice = ChoiceSerializer(choise, many=True)
        return Response({"question": serializer_question.data,
                         "choise": serializer_choice.data}, status=status.HTTP_200_OK)
    
    
class QuestionDeleteAPIView(APIView):
    '''Удаление вопросов'''

    def delete(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"}, status=405)
        que = Question.objects.get(pk=pk)
        que.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class VoteCreateAPIView(APIView):
    '''Создание выбора'''
    def post(self, request):
        pk = Choice.objects.get(pk=request.data['id'])
        vote = Vote.objects.create(choice=pk)
        return Response(status=status.HTTP_200_OK)
    

class VoteListCreateView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class StaticQuestionAPIView(APIView):

    def get(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"}, status=405)
        que = Question.objects.get(pk=pk)
        choice = Choice.objects.filter(question_id=que)

        responce = {}
        for ch in choice:
            vote = Vote.objects.filter(choice_id=ch).count()
            responce[ch.id] = vote
            
        print(responce)
        return Response(responce, status=status.HTTP_200_OK)