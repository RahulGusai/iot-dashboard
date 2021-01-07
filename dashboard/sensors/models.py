from django.db import models

# Create your models here.
class Sensor(models.Model):
    macId = models.CharField(max_length=20,unique=True,blank=False)
    battery = models.IntegerField()
    gateway = models.CharField(max_length=20,unique=True,blank=False)

class Data(models.Model):
    temp = models.IntegerField()
    humidity = models.IntegerField()
    airflow = models.IntegerField()
    timeStamp = models.CharField(max_length=20,unique=True,blank=False)

