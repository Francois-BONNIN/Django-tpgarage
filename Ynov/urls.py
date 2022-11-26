from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from myApp1.views.features import *
from myApp1.views.login import *
from myApp1.views.vehicule import *

router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # Connection
    path('signup/', CreateAccount.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    
    # Vehicule
    path('api/vehicules/', getAllVehicule.as_view()),
    path('api/vehicules/marques', getVehiculeByMarque.as_view()),

    # AdminFeatures
    path('api/vehicule/add', CreateVehicule.as_view()),
    path('api/vehicule/update', UpdateVehicule.as_view()),
    path('api/vehicule/delete', DeleteVehicule.as_view()),

    # Location
    path('api/vehicule/location', LocationVehicule.as_view()),
    path('api/vehicule/return', ReturnVehiculeLocation.as_view()),
]