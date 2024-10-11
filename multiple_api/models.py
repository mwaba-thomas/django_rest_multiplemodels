from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)  # e.g., Toyota, Ford
    model = models.CharField(max_length=100)  # e.g., Corolla, Mustang
    year = models.IntegerField()  # e.g., 2020
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

     
class AirCraft(models.Model):
    name = models.CharField(max_length=100)  # e.g., Boeing, Airbus
    model = models.CharField(max_length=100)  # e.g., 737, A320
    year_of_manufacture = models.IntegerField()  # e.g., 2015
    capacity = models.IntegerField()  # Number of passengers the aircraft can carry
    
    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year_of_manufacture})"

class Ship(models.Model):
    name = models.CharField(max_length=100)  # e.g., Titanic, Queen Mary 2
    year_built = models.IntegerField()  # e.g., 2005
    length_in_meters = models.DecimalField(max_digits=10, decimal_places=2)  # Length of the ship in meters
    capacity = models.IntegerField()  # Number of passengers the ship can carry

    def __str__(self):
        return f"{self.name} ({self.year_built})"
