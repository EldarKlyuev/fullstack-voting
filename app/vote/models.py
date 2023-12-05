from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=255, blank=False, unique=True)
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

    is_enable = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = 'public"."users'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.choice_text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'choice']