from django.db import models
from django.contrib.auth.models import User


class DailyTracking(models.Model):
    today = models.BooleanField(default=False)
    day2 = models.BooleanField(default=False)
    day3 = models.BooleanField(default=False)
    day4 = models.BooleanField(default=False)
    day5 = models.BooleanField(default=False)
    day6 = models.BooleanField(default=False)
    day7 = models.BooleanField(default=False)


class Habit(models.Model):
    title = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    catagory = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
