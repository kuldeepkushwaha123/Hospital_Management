from django.db import models

# Create your models here.

class Patient(models.Model):

    name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name




