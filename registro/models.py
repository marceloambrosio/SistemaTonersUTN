from django.db import models

# Create your models here.

class Toner(models.Model):
    nombre = models.CharField(max_length=50)

class Area(models.Model):
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)

class Impresora(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)