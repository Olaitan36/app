# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    

class Crisis(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)

class Resource(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()

class Donation(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    donor_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Volunteer(models.Model):
    crisis = models.ForeignKey(Crisis, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    availability_date = models.DateField()
