

# views.py
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status

from .models import Parroquia
from .models import SolicitudInf
                    
from .models import SolicitudCons
from .models import Contribuyentes
from .models import Establecimientos
from .models import TiposNegocios
from .models import Inspector

from  .serializer import ParroquiaSerializer
from  .serializer import ContribuyentesSerializer
from  .serializer import ContribuyentesRSerializer
from  .serializer import TiposNegociosSerializer
from  .serializer import EstablecimientosSerializer
from  .serializer import EstablecimientoSerializer
from  .serializer import InspectorSerializer
from  .serializer import SolicitudSerializer
from  .serializer import SolicitudConsSerializer
from  .serializer import SolictudEstaSerializer
from  .serializer import SolictudEstaConsSerializer


class ParroquiaViewSet(viewsets.ModelViewSet):
    queryset = Parroquia.objects.all()
    serializer_class = ParroquiaSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = SolicitudInf.objects.all()
    serializer_class = SolicitudSerializer

class SolicitudConsViewSet(viewsets.ModelViewSet):
    queryset = SolicitudCons.objects.all()
    serializer_class = SolicitudConsSerializer

class ContribuyenteViewSet(viewsets.ModelViewSet):
    queryset = Contribuyentes.objects.all()
    serializer_class = ContribuyentesSerializer

class ContribuyenteRViewSet(viewsets.ModelViewSet):
    queryset = Contribuyentes.objects.all()
    serializer_class = ContribuyentesRSerializer

class InspectorViewSet(viewsets.ModelViewSet):
    queryset = Inspector.objects.all()
    serializer_class = InspectorSerializer

class EstablemientosContribuyenteViewSet(viewsets.ModelViewSet):
    
    queryset = Establecimientos.objects.all()
    serializer_class = EstablecimientoSerializer

class solicutdEstablecimientoViewSet(viewsets.ModelViewSet):
    
    queryset = SolicitudInf.objects.all()
    serializer_class = SolictudEstaSerializer
        
class solicutdEstablecimientoConsViewSet(viewsets.ModelViewSet):
    
    queryset = SolicitudCons.objects.all()
    serializer_class = SolictudEstaConsSerializer


class TiposNegocioViewSet(viewsets.ModelViewSet):
    queryset = TiposNegocios.objects.all()
    serializer_class = TiposNegociosSerializer

class EstablecimientoViewSet(viewsets.ModelViewSet):
    queryset = Establecimientos.objects.all()
    serializer_class = EstablecimientosSerializer


class EstablecimientosInforme(viewsets.ViewSet):
       def list(self, request, contribuyente_id=None):
        if contribuyente_id is None:
            return Response({"detail": "Cliente ID no proporcionado."}, status=status.HTTP_400_BAD_REQUEST)

        ventas = Establecimientos.objects.filter(contribuyente_id=contribuyente_id)
        serializer = EstablecimientosSerializer(ventas, many=True)
        return Response(serializer.data)

class ProductoList(generics.ListAPIView):
    serializer_class = ContribuyentesRSerializer

    def get_queryset(self):
        """
        Devuelve una lista de productos filtrados por ID si se proporciona.
        """
        queryset = Contribuyentes.objects.all()
        id_param = self.request.query_params.get('id', None)
        if id_param is not None:
            queryset = queryset.filter(ruc_cont=id_param)
        return queryset