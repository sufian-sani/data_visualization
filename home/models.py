from django.db import models

# Create your models here.
class jsonModel(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=30)
    high = models.CharField(max_length=10)
    low = models.CharField(max_length=10)
    open = models.CharField(max_length=10)
    close = models.CharField(max_length=10)
    volume = models.CharField(max_length=20)