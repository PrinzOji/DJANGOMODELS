from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.name