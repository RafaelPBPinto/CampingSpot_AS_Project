from distutils.command.upload import upload
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Parque(models.Model): 
    nome = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    activities =ArrayField(ArrayField(models.CharField(max_length = 100)))
    rating = models.IntegerField()
    pricepn = models.IntegerField()
    nreservas = models.IntegerField()
    nvagas = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='parques_pics')

