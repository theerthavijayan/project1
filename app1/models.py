from django.db import models

class Users(models.Model):
    Name=models.TextField(max_length=100)
    Password=models.TextField()
    Email=models.EmailField(unique=True)
    Phone=models.BigIntegerField(unique=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class student(models.Model):
    stuName=models.TextField(max_length=100)
    stuPassword=models.TextField()
    stuEmail=models.EmailField(unique=True)
    stuPhone=models.BigIntegerField(unique=True)
    admnDate=models.DateField()

