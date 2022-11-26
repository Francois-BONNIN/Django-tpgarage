# Generated by Django 4.1.2 on 2022-11-25 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0008_location_prixfinal_alter_vehicule_marque'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='kilometrageDepart',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='kilometrageRetour',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='conducteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myApp1.conducteur'),
        ),
        migrations.AlterField(
            model_name='location',
            name='dateFin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='prixFinal',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='vehicule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myApp1.vehicule'),
        ),
    ]