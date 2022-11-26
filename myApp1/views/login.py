from django.core import serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..models import *
from ..serializers import *


class CreateAccount(APIView):
    def put(self, request):
        data = request.data
        conducteur = Conducteur.objects.create(
            login = data['login'],
            nom=data['nom'],
            prenom=data['prenom'],
            dateNaissance=data['dateNaissance'],
            civilite=data['civilite'],
            password=data['password'],
        )
        conducteur.save()
        return Response({"message": "Compte créé avec succès"})

class Login(APIView):
    def put(self, request):
        data = request.data
        conducteur = Conducteur.objects.filter(login=data['login'], password=data['password'])
        administrateur = Administrateur.objects.filter(login=data['login'], password=data['password'])
        if conducteur or administrateur:
            if conducteur :
                user = conducteur[0]
            elif administrateur :
                user = administrateur[0]
            return Response({"message": "Connexion réussie", "user":{"user": user.id, "is_admin": user.is_admin}})
        else:
            return Response({"message": "Erreur de connexion"})


class Logout(APIView):
    def post(self, request):
        data = request.data
        conducteur = Conducteur.objects.filter(id=data['user_id'])
        administrateur = Administrateur.objects.filter(id=data['user_id'])
        if conducteur or administrateur:
            return Response({"message": "Déconnexion réussie"})
        else:
            return Response({"message": "Erreur de déconnexion"})