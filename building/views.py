from .serializers import *
from .models import *

from rest_framework.viewsets import *

class HududApiList(ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer


class QurilishTashkilotiApiList(ModelViewSet):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer


class QurilishBinosiApiList(ModelViewSet):
    queryset = QurilishBinosi.objects.all()
    serializer_class = QurilishBinosiSerializer

