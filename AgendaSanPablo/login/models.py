from django.db import models

# Create your models here.

class persona(models.Model):
    nombre =  models.CharField(max_length=30)
    #apellidoPaterno = models.CharField(max_length=30)
    apellidoMaterno = models.CharField(max_length=30)
    carrera = models.IntegerField()
    email = models.CharField(max_length=40)
    secso = models.CharField(max_length=2)
