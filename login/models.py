from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Unregistered"),(1, "Registered"),)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
