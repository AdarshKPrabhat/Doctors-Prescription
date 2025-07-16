from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your models here.

class Doctor(models.Model):
    email = models.CharField(max_length=250)
    firtname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    degree  = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="uploaded_images")
    mobile = models.IntegerField()
    password = models.CharField(max_length=20)

def Patient(models.Model):
    Name = models.CharField(max_length=250)
    symptoms = models.CharField(max_length=250)
    Diagnosis = models.CharField(max_length=250)
    Prescription = models.CharField(max_length=250)
    advice = models.CharField(max_length=250)

