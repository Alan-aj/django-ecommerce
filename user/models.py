from django.db import models

# Create your models here.
class signup(models.Model):
    signid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
