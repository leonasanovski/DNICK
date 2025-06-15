from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class RealEstate(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    surface = models.FloatField(blank=True, null=True)
    publishing_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    isReserved = models.BooleanField(default=False)
    isSold = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'


class Agent(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=9, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    sold_real_estates = models.IntegerField(blank=True, null=True, default=0)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class AgentRealEstate(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)


class Characteristic(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class CharacteristicRealEstate(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

