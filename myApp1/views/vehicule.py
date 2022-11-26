from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..auth import *

from ..models import *
from ..serializers import *

class getAllVehicule(APIView):
    def get(self, request):
        # if (isLogin(request.data["user_id"])):
            vehicules = Vehicule.objects.all()
            serializer = VehiculeSerializer(vehicules, many=True)
            return Response(serializer.data)
        # else:
        #     return Response({"message": "Vous n'avez pas les droits pour accéder à cette ressource"})

class getVehiculeByMarque(APIView):
    def get(self, request):
        if (isLogin(request.data["user_id"])):
            vehicules = Vehicule.objects.filter(marque=request.data["marque"])
            serializer = VehiculeSerializer(vehicules, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Vous n'avez pas les droits pour accéder à cette ressource"})


class CreateVehicule(APIView):
    def put(self, request):
        if (isAdmin(request.data["user_id"])):
            data = request.data
            vehicule = Vehicule.objects.create(
                marque = data['marque'],
                modele = data['modele'],
                kilometrage = data['kilometrage'],
                prixjournalier = data['prixjournalier'],
                statut = data['statut'],
            )
            vehicule.save()
            return Response({"message": "Véhicule créé avec succès"})
        else:
            return Response({"message": "Vous n'avez pas les droits pour accéder à cette ressource"})

class UpdateVehicule(APIView):
    def post(self, request):
        if (isAdmin(request.data["user_id"])):
            data = request.data
            vehicule = Vehicule.objects.get(id=data['id'])
            vehicule.marque = data['marque']
            vehicule.modele = data['modele']
            vehicule.kilometrage = data['kilometrage']
            vehicule.prixjournalier = data['prixjournalier']
            vehicule.statut = data['statut']
            vehicule.save()
            return Response({"message": "Véhicule modifié avec succès"})
        else:
            return Response({"message": "Vous n'avez pas les droits pour accéder à cette ressource"})

class DeleteVehicule(APIView):
    def delete(self, request):
        if (isAdmin(request.data["user_id"])):
            data = request.data
            vehicule = Vehicule.objects.get(id=data['id'])
            vehicule.delete()
            return Response({"message": "Véhicule supprimé avec succès"})
        else:
            return Response({"message": "Vous n'avez pas les droits pour accéder à cette ressource"})
