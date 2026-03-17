
from rest_framework import serializers
from  .models import Informes
from  .models import Informeimagen
from  .models import InformesDetalle
from  .models import InformeExtintor
from contribuyentes.models import Establecimientos
from contribuyentes.serializer import EstablecimientoSerializer
from contribuyentes.serializer import InspectorSerializer

from  .models import InformesConsturccion
from  .models import InformesDetalleCons


class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informes
        fields = '__all__'

class InformeConstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformesConsturccion
        fields = '__all__'


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informeimagen
        fields = ['informe','descripcion','imagen']
    
    def validate_informe(self, value):
        # Aquí puedes agregar validaciones adicionales si es necesario
        if not Informes.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El informe especificado no existe.")
        return value

class EstablecimientoInformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informes
        fields = '__all__'
    
    def validate_informeE(self, value):
        # Aquí puedes agregar validaciones adicionales si es necesario
        if not Establecimientos.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El Esytablecimiento especificado no existe.")
        return value

class InformeISerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True, read_only=True)
    
    class Meta:
        model = Informes
        fields = ['id', 'numero_informe','inspector','establecimiento','nrosocilitud','resultado_informe', 'observacion', 'imagenes']


class InformesSerializer(serializers.ModelSerializer):
    
    establecimientoI = InformeSerializer(many=True)
    class Meta:
        model = Establecimientos
        fields =  ['id','nombre_est','establecimientoI']
  



class InformeDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformesDetalle
        fields = '__all__'

class InformeDetalleConstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformesDetalleCons
        fields = '__all__'

class InformeExtintorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformeExtintor
        fields = '__all__'

class InformesRSerializer(serializers.ModelSerializer):
    detalleinforme = InformeDetalleSerializer(many=True, read_only=True)
    class Meta:
        model = Informes
        fields =  ['fecha_informe','numero_informe','resultado_informe','detalleinforme']

