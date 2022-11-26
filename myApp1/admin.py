from django.contrib import admin
from .models import *

admin.site.register(Conducteur)
admin.site.register(Administrateur)
admin.site.register(Vehicule)
admin.site.register(Location)