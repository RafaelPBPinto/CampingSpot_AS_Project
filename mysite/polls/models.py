from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.contrib.auth.models import User

class Parque(models.Model): 
    nome = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    activities = models.CharField(max_length = 20)
    rating = models.IntegerField()
    pricepn = models.FloatField()
    nreservas = models.IntegerField()
    nvagas = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='parque_pics')

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    parque = models.ForeignKey(Parque, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    datei = models.DateField()
    datef = models.DateField()
    activity = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return self.parque + '; ' + self.client 
