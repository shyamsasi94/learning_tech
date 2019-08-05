from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ShipOwner(models.Model):
    name = models.CharField(max_length=50)
    ph_no = models.CharField(max_length=12)
    profile = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=50)
    length = models.FloatField()
    breadth = models.FloatField()
    owner = models.ForeignKey(ShipOwner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShipCharter(models.Model):
    name = models.CharField(max_length=50)
    ship_owner = models.ManyToManyField(ShipOwner)

    def __str__(self):
        return self.name
