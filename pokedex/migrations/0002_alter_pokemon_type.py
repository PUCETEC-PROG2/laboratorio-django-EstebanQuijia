# Generated by Django 4.2 on 2025-01-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('X', 'Xavi'), ('A', 'Agua'), ('E', 'Electrico'), ('T', 'Tierra'), ('F', 'Fuego')], max_length=30),
        ),
    ]