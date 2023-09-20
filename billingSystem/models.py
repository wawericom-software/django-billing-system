from django.db import models

class user(models.Model):
    username = models.CharField(max_length=225)
    password = models.IntegerField()