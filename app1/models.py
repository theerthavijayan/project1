from django.db import models

class Users(models.Model):
    Name=models.TextField(max_length=100)
    Password=models.TextField()
    Email=models.EmailField(unique=True)
    Phone=models.BigIntegerField(unique=True)
