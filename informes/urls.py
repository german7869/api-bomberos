from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import InformeViewSet
from .views import InformesViewSet 

from .views import InformesConstruccionViewSet 
from .views import InformesDetalleConstruccionViewSet 

from .views import ImagenViewSet
from .views import InformeDetalleViewSet
from .views import InformeExtintorViewSet
from .views import EstablecminetoinformeViewSet


router = DefaultRouter()

router.register(r'listadoinfo/',InformesViewSet)
router.register(r'listadoinfocons/',InformesConstruccionViewSet)
router.register(r'listadoinfo/(?P<establecimiento_id>\d+)/informe', InformeViewSet, basename='informeE')
router.register(r'listadoinfocons/(?P<contribuyente_id>\d+)/informe', InformesConstruccionViewSet, basename='informecons')
router.register(r'listadoinfo/(?P<establecimiento_id>\d+)/establecimiento', EstablecminetoinformeViewSet, basename='EstablecimientoI')
router.register(r'listadoinfo/(?P<informe_id>\d+)/imagenes', ImagenViewSet, basename='imagenes')
router.register(r'DetalleI/(?P<informe_id>\d+)/informe', InformeDetalleViewSet, basename='informedet')
router.register(r'DetalleIcons/(?P<informe_id>\d+)/informe', InformesDetalleConstruccionViewSet, basename='informedetcons')

router.register(r'DetalleE/(?P<informe_id>\d+)/informe', InformeExtintorViewSet, basename='informedetE')
router.register(r'DetalleEcons/',InformesDetalleConstruccionViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
