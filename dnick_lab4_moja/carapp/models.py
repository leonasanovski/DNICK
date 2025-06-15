from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_of_establishment = models.IntegerField()
    num_of_employees = models.IntegerField()
    def __str__(self):
        return f'{self.name} - {self.year_of_establishment}'

class Car(models.Model):
    TYPE_OF_CAR = [
        ("SUV", "SUV"),
        ("sedan", "sedan"),
        ("hatchback", "hatchback"),
        ("coupe", "coupe"),
    ]
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    price = models.IntegerField()
    chassis_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year_of_production = models.IntegerField()
    type = models.CharField(max_length=15, choices=TYPE_OF_CAR, default="SUV")
    car_image = models.ImageField(upload_to="car_images/", null=True, blank=True)
    def __str__(self):
        return f'{self.model} - {self.manufacturer.name}'