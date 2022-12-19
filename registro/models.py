from django.db import models

# Create your models here.

class Toner(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Impresora(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca + " - " + self.modelo