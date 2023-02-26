from django.db import models

from datetime import date

# Create your models here.

class Author(models.Model):
    #models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)


    def __str__(self):
        return self.name
    

class Entry(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    headline = models.CharField(max_length=150)
    bodyText = models.TextField()
    publicDate = models.DateField(default=date.today)
    rating = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.headline
    
