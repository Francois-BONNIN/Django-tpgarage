# Generated by Django 4.1 on 2022-08-16 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=30)),
                ('style', models.CharField(choices=[('POP', 'Pop'), ('RAP', 'Rap'), ('CLA', 'Classique'), ('ROK', 'Rock'), ('UND', 'Indéfini')], default='UND', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Chanson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField(max_length=30)),
                ('duree', models.FloatField(default=0.0)),
                ('date', models.DateField()),
                ('artiste', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myApp1.artiste')),
            ],
        ),
    ]