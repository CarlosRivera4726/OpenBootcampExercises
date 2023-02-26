from django.db import models

# Create your models here.
class Directores(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return "Director: " + self.first_name + " " + self.last_name