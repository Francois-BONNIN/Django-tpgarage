# Generated by Django 4.1.2 on 2022-11-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0007_conducteur_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='prixFinal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='marque',
            field=models.CharField(choices=[('RENAULT', 'Renault'), ('PEUGEOT', 'Peugeot'), ('CITROEN', 'Citroen'), ('VOLKSWAGEN', 'Volkswagen'), ('MERCEDES', 'Mercedes'), ('BMW', 'BMW'), ('AUDI', 'Audi')], default='UNDEFINED', max_length=50),
        ),
    ]