from .models import *
from .serializers import *

def isLogin(id):
    conducteur = Conducteur.objects.filter(id=id)
    administrateur = Administrateur.objects.filter(id=id)
    if conducteur or administrateur:
        return True
    else:
        return False


def isAdmin(id):
    administrateur = Administrateur.objects.filter(id=id)
    if administrateur:
        return True
    else:
        return False
