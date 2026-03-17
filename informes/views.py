

# views.py
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Informes
from  .models import InformesConsturccion
from  .models import InformesDetalleCons


from .models import Informeimagen
from .models import InformesDetalle
from .models import InformeExtintor


from  .serializer import InformesSerializer
from  .serializer import ImagenSerializer
from  .serializer import InformeSerializer
from  .serializer import EstablecimientoInformeSerializer
from  .serializer import InformeDetalleSerializer
from  .serializer import InformeExtintorSerializer

from  .serializer import InformeConstruccionSerializer
from  .serializer import InformeDetalleConstruccionSerializer

class  InformeViewSet(viewsets.ModelViewSet):
    queryset = Informes.objects.all()
    serializer_class = InformeSerializer 
    def get_queryset(self):
        establecimiento_id = self.kwargs.get('establecimiento_id')
        if establecimiento_id:
            return Informes.objects.filter(establecimiento_id=establecimiento_id)
        return Informes.objects.none()  # Devuelve un queryset vacío si no hay informe_id

class  InformesViewSet(viewsets.ModelViewSet):
    queryset = Informes.objects.all()
    serializer_class = InformeSerializer 
    

class  InformesConstruccionViewSet(viewsets.ModelViewSet):
    queryset = InformesConsturccion.objects.all()
    serializer_class = InformeConstruccionSerializer 

class  InformesDetalleConstruccionViewSet(viewsets.ModelViewSet):
    queryset = InformesDetalleCons.objects.all()
    serializer_class = InformeDetalleConstruccionSerializer 

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Informeimagen.objects.all()
    serializer_class = ImagenSerializer
    def get_queryset(self):
        informe_id = self.kwargs.get('informe_id')
        if informe_id:
            return Informeimagen.objects.filter(informe_id=informe_id)
        return Informeimagen.objects.none()  # Devuelve un queryset vacío si no hay informe_id
   
class EstablecminetoinformeViewSet(viewsets.ModelViewSet):
    queryset = Informes.objects.all()
    serializer_class = EstablecimientoInformeSerializer
    def get_queryset(self):
        establecimiento_id = self.kwargs.get('establecimiento_id')
        if establecimiento_id:
            return Informes.objects.filter(establecimiento_id=establecimiento_id)
        return Informes.objects.none()  # Devuelve un queryset vacío si no hay informe_id

class InformeDetalleViewSet(viewsets.ModelViewSet):
    queryset = InformesDetalle.objects.all()
    serializer_class = InformeDetalleSerializer

class InformeExtintorViewSet(viewsets.ModelViewSet):
    queryset = InformeExtintor.objects.all()
    serializer_class = InformeExtintorSerializer

