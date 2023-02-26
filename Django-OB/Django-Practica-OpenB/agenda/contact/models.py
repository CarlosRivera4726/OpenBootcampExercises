from django.db import models
from datetime import date

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    mobile = models.CharField(max_length=13, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    company = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=date.today)
    notes = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name
    