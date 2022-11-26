
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..auth import *

from ..models import *
from ..serializers import *

class LocationVehicule(APIView):
    def put(self, request):
        if (isLogin(request.data["user_id"])):
            data = request.data
            vehicule = Vehicule.objects.get(id=data['vehicule'])
            location = Location.objects.create(
                vehicule = data['vehicule'],
                conducteur = data['conducteur'],
                dateDebut = data['dateDebut'],
                kilometrageDebut = vehicule.kilometrage,
            )
            location.save()
            vehicule.statut = "LOUE"
            vehicule.save()
            return Response({"message": "Location créée avec succès"})
        else:
            return Response({"message": "Vous n'avez pas les droits pour accéder à cette ressource"})


class ReturnVehiculeLocation(APIView):
    def put(self, request):
        if (isLogin(request.data["user_id"])):
            data = request.data
            location = Location.objects.get(id=data['id'])
            location.dateFin = data['dateFin']
            location.kilometrageRetour = data['kilometrageRetour']
            location.prixFinal = (location.dateFin - location.dateDebut).days * location.vehicule.prixjournalier
            location.save()

            vehicule = Vehicule.objects.get(id=data['vehicule'])
            vehicule.kilometrage = data['kilometrageRetour']
            vehicule.statut = "DISPONIBLE"
            vehicule.save()
            return Response({"message": "Location terminée avec succès", "prixFinal": location.prixFinal})




# class ChansonViewset(ModelViewSet):
  
#   serializer_class = ChansonSerializer

#   def get_queryset(self):
#     queryset = Chanson.objects.all()
#     return queryset
