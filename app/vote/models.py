from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=255, blank=False, unique=True)
    username = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    ROLE_CHOISES = [
        ('Admin', 'Admin'),
        ('User', 'User')
    ]
    role_sys = models.CharField(max_length=20,
                                choices=ROLE_CHOISES,
                                default=ROLE_CHOISES[1][1],
                                null=True)
    
    is_enable = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = 'public"."users'


class Voting(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    class Meta:
        db_table = 'public"."voting'


# class VotingChoises
