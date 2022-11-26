from rest_framework.serializers import ModelSerializer
from .models import *

class VehiculeSerializer(ModelSerializer):
    class Meta:
        model = Vehicule
        fields = ['id', 'marque', 'modele', 'kilometrage', 'prixjournalier', 'statut']


class ConducteurSerializer(ModelSerializer):
    class Meta:
        model = Conducteur
        fields = ['id', 'nom', 'prenom', 'dateNaissance', 'civilite']
      
class LocationSerializer(ModelSerializer):
  vehicule = VehiculeSerializer(many=True)
  conducteur = ConducteurSerializer(many=True)
  class Meta:
      model = Location
      fields = ['id', 'vehicule', 'conducteur', 'dateDebut', 'dateFin']