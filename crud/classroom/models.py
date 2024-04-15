from django.db import models

# Create your models here.
class Student(models.Model):
  nama = models.CharField(max_length=200)
  kelas=models.CharField(max_length=200)
