from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    age = models.IntegerField(default=0)


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)
