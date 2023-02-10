from django.db import models
from registro.models import Toner

# Create your models here.

class TonerPorArea(models.Model):
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE)

    def __str__(self):
        return self.toner.nombre