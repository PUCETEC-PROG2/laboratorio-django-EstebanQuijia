# Generated by Django 4.2 on 2025-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('X', 'Xavi'), ('A', 'Agua'), ('E', 'Electrico'), ('F', 'Fuego'), ('P', 'Planta')], max_length=30),
        ),
    ]