# Generated by Django 4.0.5 on 2022-06-07 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_atividades_remove_parques_atv1_remove_parques_atv2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parques',
            name='activities',
            field=models.ForeignKey(default='Arvorismo', on_delete=django.db.models.deletion.CASCADE, to='polls.atividades'),
        ),
    ]
