from django.db import models

# Create your models here.

class Toner(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre + " (" + str(self.stock) + ")"

class Area(models.Model):
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " (" + self.responsable + ")"

class Impresora(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.area.nombre + " - " + self.marca + " " + self.modelo + " (" + self.toner.nombre + ")"

class Registro(models.Model):
    fecha = models.DateField()
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return self.fecha + self.impresora + "Cantidad: " + self.cantidad