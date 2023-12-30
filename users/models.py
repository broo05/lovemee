# appname/models.py
from django.db import models

class LoveTest(models.Model):
    girl_name = models.CharField(max_length=100)
    boy_name = models.CharField(max_length=100)
    love_percentage = models.IntegerField()

    def __str__(self):
        return f"{self.girl_name} and {self.boy_name} - {self.love_percentage}%"
