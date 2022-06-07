from django.db import models

class Atividades(models.Model):
    atvs = models.TextField()

class Parques(models.Model): 
    nome = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    activities = models.ForeignKey(Atividades, on_delete=models.CASCADE)
    rating = models.IntegerField()
    pricepn = models.IntegerField()
    nreservas = models.IntegerField()
    nvagas = models.IntegerField()
    image = models.ImageField(default='default.jpg')


