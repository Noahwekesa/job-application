from django.db import models

# Create your models here.

class Application(models.Model):
    positon =  models.CharField(max_length=50)
