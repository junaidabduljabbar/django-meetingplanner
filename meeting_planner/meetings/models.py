from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()