from django.db import models

from contribuyentes import models as contribuyentes_models

class Informes(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha_informe = models.DateTimeField(auto_now=True)
    numero_informe = models.IntegerField(null=False, default=None)
    resultado_informe = models.CharField(max_length=250,null=False, default=None)
    observacion=models.CharField(max_length=250,null=True)
    recomendaciones=models.CharField(max_length=250,null=True)
   
   


   
    
    establecimiento =  models.ForeignKey(contribuyentes_models.Establecimientos,related_name='establecimientoI', on_delete=models.CASCADE, default=None)
    nrosocilitud = models.IntegerField(null=False,default=None)
    tamano =models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.resultado_informe

    class Meta:
        db_table = 'informes'  # Custom table name
    
class Informeimagen(models.Model):
   
    descripcion=models.CharField(max_length=250,null=True)
    imagen = models.ImageField(upload_to='images/',default=None)
    informe =  models.ForeignKey(Informes,related_name='imagenes', on_delete=models.CASCADE, default=None)
    
    

    def __str__(self):
        return self.imagen_informe
    class Meta:
        db_table = 'informeimagen'  # Custom table name


class InformesDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250,null=False)
    valor = models.BooleanField(default=True)
    categoria = models.CharField(max_length=100,null=False,default='varios')
    informe  =  models.ForeignKey(
        'Informes',
        on_delete=models.CASCADE,
        related_name='informed',
        null=False)
    
   

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'informe_detalle'  # Custom table name


class InformeExtintor(models.Model):

    informe   =  models.ForeignKey(
        'Informes',
        on_delete=models.CASCADE,
        related_name='informee',
        null=False)
    cantidad = models.IntegerField(), 
    tipo = models.CharField(max_length=250,null=False)
    estado = models.CharField(max_length=250,null=False)
    capacidad = models.CharField(max_length=250,null=False)
    fecha_caducidad =  models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True) 

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'ininforme_det_extintor'  # Custom table name

class InformesConsturccion(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha_informe = models.DateTimeField(auto_now=True)
    numero_informe = models.IntegerField(null=False, default=None)
    resultado_informe = models.CharField(max_length=250,null=False, default=None)
    observacion=models.CharField(max_length=250,null=True)
    recomendaciones=models.CharField(max_length=250,null=True)
    tipoconstruccion=models.CharField(max_length=250,null=True)
    arealote=models.CharField(max_length=250,null=True)
    tipoesctructura=models.CharField(max_length=250,null=True)
    tamaño=models.CharField(max_length=250,null=True)
    nroplantaconstruidas=models.CharField(max_length=250,null=True)
    nroplantaenconstruccion=models.CharField(max_length=250,null=True)
    areaconstruccion=models.CharField(max_length=250,null=True)
    establecimiento =  models.ForeignKey(contribuyentes_models.Establecimientos,related_name='establecimientoIcon', on_delete=models.CASCADE, default=None)
    nrosocilitud = models.IntegerField(null=False,default=None)
    

    def __str__(self):
        return self.resultado_informe

    class Meta:
        db_table = 'informescons'  # Custom table name

class InformesDetalleCons(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250,null=False)
    valor = models.BooleanField(default=True)
    categoria = models.CharField(max_length=100,null=False,default='varios')
    informe  =  models.ForeignKey(
        'InformesConsturccion',
        on_delete=models.CASCADE,
        related_name='informec',
        null=False)
    
   

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'informe_detalle_cons'  # Custom table name
