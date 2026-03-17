from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import ContribuyenteViewSet
from .views import ContribuyenteRViewSet
from .views import EstablecimientoViewSet
from .views import InspectorViewSet
from .views import SolicitudViewSet
from .views import SolicitudConsViewSet

from .views import ProductoList
from .views import ParroquiaViewSet
from .views import TiposNegocioViewSet
from .views import EstablemientosContribuyenteViewSet
from .views import solicutdEstablecimientoViewSet
from .views import solicutdEstablecimientoConsViewSet





router = DefaultRouter()
router.register(r'contesta/(?P<contribuyente_id>[^/.]+)/esta', EstablemientosContribuyenteViewSet, basename='estcont')
router.register(r'listadoC/',ContribuyenteViewSet,basename='listadoC')
router.register(r'listador/',ContribuyenteRViewSet,basename='listadoR')
router.register(r'listadoe/',EstablecimientoViewSet,basename='Establecimientosl')
router.register(r'listadoec/',EstablemientosContribuyenteViewSet,basename='EstablecimientoslC')
router.register(r'listadoins/',InspectorViewSet,basename='inspectorl')
router.register(r'listadopar/',ParroquiaViewSet,basename='parroquial')
router.register(r'listadotip/',TiposNegocioViewSet,basename='tipol')
router.register(r'listadoSolicitud/',SolicitudViewSet,basename='solicitud')
router.register(r'listadoSolicitude/',solicutdEstablecimientoViewSet,basename='solicitude')
router.register(r'listadoSolicitudcons/',SolicitudConsViewSet,basename='solicitudcons')
router.register(r'listadoSolicitudconse/',solicutdEstablecimientoConsViewSet,basename='solicitudconse')

 




urlpatterns = [
    path('',include(router.urls)),
    path('productos/', ProductoList.as_view(), name='producto-list'),   

]
