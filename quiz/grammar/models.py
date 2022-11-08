from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Questions(models.Model):
    qst = models.CharField(max_length=200)
    no = models.IntegerField(unique=True)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
    time = models.IntegerField(default=90)

    def __str__(self):
        return self.qst


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.FloatField(default=0)
    score = models.IntegerField(default=0)
    no = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user)