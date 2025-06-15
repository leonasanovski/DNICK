from tkinter.constants import CASCADE

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Baker(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.name} {self.surname}'

class Cake(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    cake_image = models.ImageField(upload_to='cakes', null=True, blank=True)
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')
    #related name is to get all the cakes of that baker
    def __str__(self):
        return f'{self.name} - {self.price} den'