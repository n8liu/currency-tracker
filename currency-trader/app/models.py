from django.db import models

# Create your models here.
class Candle(models.Model):
    complete = models.CharField(max_length=10, default='empty')
    volume = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    o = models.CharField(max_length=50)
    h = models.CharField(max_length=50)
    l = models.CharField(max_length=50)
    c = models.CharField(max_length=50)

class Aroon(models.Model):
    up = models.CharField(max_length=30)
    down = models.CharField(max_length=30)

class Atr(models.Model):
    atr = models.CharField(max_length=20)

class Chaikin(models.Model):
    ad = models.CharField(max_length=20)

class Sma(models.Model):
    high = models.CharField(max_length=20)
    low = models.CharField(max_length=20)
    close = models.CharField(max_length=20)

class Ssl(models.Model):
    ssl = models.CharField(max_length=20)