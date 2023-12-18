from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''Таблица пользователя'''

    username = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User')
    ]
    role_sys = models.CharField(max_length=20,
                                choices=ROLE_CHOICES,
                                default=ROLE_CHOICES[1][1],
                                null=True)

    def __str__(self) -> str:
        return self.username


class Question(models.Model):
    '''Вопросы'''

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    '''Выборы'''

    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.choice_text


class Vote(models.Model):
    '''Голоса'''

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'choice']