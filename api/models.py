from django.db import models

class ApiCrud(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
