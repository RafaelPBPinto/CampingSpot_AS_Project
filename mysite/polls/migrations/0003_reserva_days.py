# Generated by Django 4.0.5 on 2022-06-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_reserva_npessoas'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='days',
            field=models.IntegerField(default=1),
        ),
    ]