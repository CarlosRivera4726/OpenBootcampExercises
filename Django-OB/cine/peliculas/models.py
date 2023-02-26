from django.db import models
import directores.models

# Create your models here.
class Peliculas(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    director = models.ForeignKey(directores.models.Directores, on_delete=models.CASCADE)
    def __str__(self):
        return self.name