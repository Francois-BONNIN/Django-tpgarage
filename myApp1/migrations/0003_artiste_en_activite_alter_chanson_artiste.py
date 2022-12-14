# Generated by Django 4.1 on 2022-08-23 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0002_alter_artiste_nom_alter_chanson_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='en_activite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chanson',
            name='artiste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chansons', to='myApp1.artiste'),
        ),
    ]
