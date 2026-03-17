
from rest_framework import serializers

from  .models import Contribuyentes
from  .models import Establecimientos
from  .models import Parroquia
from  .models import TiposNegocios
from  .models import Inspector
from  .models import SolicitudInf
from  .models import SolicitudCons


from  .models import Establecimientos

class ContribuyentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyentes
        fields = '__all__'
        
class EstablecimientoSerializer(serializers.ModelSerializer):
    contribuyente = ContribuyentesSerializer(read_only=True)
    class Meta:
        model = Establecimientos
        fields = '__all__' 

class EstablecimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimientos
        fields = '__all__'

class SolictudEstaSerializer(serializers.ModelSerializer):
    establecimiento = EstablecimientosSerializer(read_only=True)
    class Meta:
        model = SolicitudInf
        fields = '__all__' 

class SolictudEstaConsSerializer(serializers.ModelSerializer):
    contribuyente = ContribuyentesSerializer(read_only=True)
    class Meta:
        model = SolicitudCons
        fields = '__all__' 




class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquia
        fields = '__all__'       

class TiposNegociosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposNegocios
        fields = '__all__'   

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudInf
        fields = '__all__'   

class SolicitudConsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCons
        fields = '__all__'   


class   InspectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspector
        fields = '__all__'       

class ContribuyentesRSerializer(serializers.ModelSerializer):
    contribuyenteE = EstablecimientoSerializer(many=True)
    class Meta:
        model = Contribuyentes
        fields = '__all__'       


class InformeESerializer(serializers.ModelSerializer):
    contribuyenteE = EstablecimientoSerializer(many=True)
    class Meta:
        model = Contribuyentes
        fields =  ['ruc_cont','nombre_cont','direccion_cont','email_cont','contribuyenteE']

