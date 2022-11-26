from django.db import models

class Vehicule(models.Model):
  MARQUE = [
    ('RENAULT', 'Renault'),
    ('PEUGEOT', 'Peugeot'),
    ('CITROEN', 'Citroen'),
    ('VOLKSWAGEN', 'Volkswagen'),
    ('MERCEDES', 'Mercedes'),
    ('BMW', 'BMW'),
    ('AUDI', 'Audi')
  ]
  STATUT = [
    ('DISPONIBLE', 'Disponible'),
    ('LOUE', 'Loué'),
    ('INDISPONIBLE', 'Indisponible'),
  ]

  marque = models.CharField(max_length=50, default='UNDEFINED', choices=MARQUE)
  modele = models.CharField(max_length=50, default='UNDEFINED')
  kilometrage = models.IntegerField(default=0)
  prixjournalier= models.FloatField(default=0)
  statut = models.CharField(max_length=50, default='DISPONIBLE', choices=STATUT)


class Conducteur(models.Model):
  CIVILITE = [
    ('M', 'Monsieur'),
    ('MME', 'Madame'),
  ]
  nom = models.CharField(max_length=50, default='UNDEFINED')
  prenom = models.CharField(max_length=50, default='UNDEFINED')
  dateNaissance = models.DateField()
  login = models.CharField(max_length=50)
  password = models.CharField(max_length=300)
  civilite = models.CharField(max_length=50, default='UNDEFINED', choices=CIVILITE)
  is_admin = models.BooleanField(default=False)

class Administrateur(models.Model):
  CIVILITE = [
    ('M', 'Monsieur'),
    ('MME', 'Madame'),
  ]
  nom = models.CharField(max_length=50, default='UNDEFINED')
  prenom = models.CharField(max_length=50, default='UNDEFINED')
  dateNaissance = models.DateField()
  login = models.CharField(max_length=50)
  password = models.CharField(max_length=300)
  civilite = models.CharField(max_length=50, default='UNDEFINED', choices=CIVILITE)
  is_admin = models.BooleanField(default=True)


class Location(models.Model):
  vehicule = models.ForeignKey('Vehicule', on_delete=models.DO_NOTHING, null=True, blank=True)
  conducteur = models.ForeignKey('Conducteur', on_delete=models.DO_NOTHING, null=True, blank=True)
  dateDebut = models.DateField()
  dateFin = models.DateField(null=True, blank=True)
  prixFinal = models.FloatField(default=0, null=True, blank=True)
  kilometrageDepart = models.IntegerField(default=0)
  kilometrageRetour = models.IntegerField(default=0)

