# Generated by Django 4.2 on 2025-01-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('F', 'Fuego'), ('X', 'Xavi'), ('E', 'Electrico'), ('P', 'Planta'), ('A', 'Agua')], max_length=30),
        ),
    ]
