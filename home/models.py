from django.db import models

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField(default="")  

class Intinerary(models.Model):
    label = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    level = models.IntegerField()
    description = models.TextField(default="")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

class Area(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")

class Country(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    FAQ = models.JSONField()
    description = models.TextField(default="")

class Destination(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.JSONField()
    activities = models.JSONField()

class Tour(models.Model):
    start_point = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="startpoint")
    end_point = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="endpoint")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="destination")

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)