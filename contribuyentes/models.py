from django.db import models



class Parroquia(models.Model):
   
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=13,null=False)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'parroquia'  # Custom table name

class Contribuyentes(models.Model):
   
    ruc_cont = models.CharField(max_length=13,primary_key=True,null=False)
    nombre_cont = models.CharField(max_length=150,null=False)
    direccion_cont = models.CharField(max_length=150,null=False)
    referencia_cont = models.CharField(max_length=150,null=False,default='N')
    email_cont = models.CharField(max_length=150,null=True)
    razon_social_cont = models.CharField(max_length=150,null=False,default='N')
    telefono_cont = models.CharField(max_length=150,null=True)
    celular_cont= models.CharField(max_length=150,null=True)
    activo = models.CharField(max_length=150,null=False,default='V')
    representante = models.CharField(max_length=150,null=True)
    parroquia_id = models.CharField(max_length=10,null=True)
   
    def __str__(self):
        return self.nombre_cont

    class Meta:
        db_table = 'contribuyentes'  # Custom table name

class TiposNegocios(models.Model):
    codigo = models.CharField(max_length=13,primary_key=True,null=False)
    anio_desde  = models.IntegerField() 
    nombre_tip = models.CharField(max_length=250,null=False)
    id_categoria = models.CharField(max_length=5,null=False)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    tipo_lugar = models.CharField(max_length=5,null=False)
    anio_hasta = models.IntegerField() 
    mes_desde = models.IntegerField() 
    mes_hasta = models.IntegerField() 
    id_clase = models.CharField(max_length=5,null=False)
    def __str__(self):
        return self.nombre_tip

    class Meta:
        db_table = 'tipo_negocio'  # Custom table name

class Inspector(models.Model):
    id =  models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=250,null=False)
    nombre_insp = models.CharField(max_length=250,null=False)
    direccion_insp = models.CharField(max_length=250,null=False)
    email_insp = models.CharField(max_length=250,null=False)
    telefono_insp = models.CharField(max_length=250,null=False)
    celular_insp = models.CharField(max_length=250,null=False)
    activo = models.CharField(max_length=250,null=False)
    
    def __str__(self):
        return self.nombre_insp

    class Meta:
        db_table = 'inspector'  # Custom table name


class Establecimientos(models.Model):
    
    id =  models.AutoField(primary_key=True)
    contribuyente =  models.ForeignKey(Contribuyentes,on_delete=models.CASCADE,
        related_name='contribuyenteE',
        null=False)
    direccion_est = models.CharField(max_length=150,null=True)
    refeencia_est = models.CharField(max_length=150,null=True,default='N')
    nombre_est = models.CharField(max_length=250,null=True)
    fec_apertura = models.DateField(auto_now_add=True)
    fecha_cierre = models.DateField(auto_now_add=True)
    estado_est = models.CharField(max_length=1,default='V')
    tipo_negocio  = models.ForeignKey(TiposNegocios,
        on_delete=models.CASCADE,
        related_name='tipo',
        null=False)
    telefono_est =  models.CharField(max_length=20,null=True)
    actividad =  models.CharField(max_length=250,null=False)
    estado = models.CharField(max_length=5,null=False,default='ABR')
    descuento = models.DecimalField( max_digits=7, decimal_places=2,default=0)
    parroquia = models.ForeignKey(Parroquia,
        on_delete=models.CASCADE,
        related_name='parroquiaE',
        null=False)
    def __str__(self):
         return self.nombre_est

    class Meta:
        db_table = 'establecimientos'  # Custom table name

class SolicitudInf(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateTimeField(auto_now=True)
    numero_soicitud = models.IntegerField(null=False, default=None)
    establecimiento =  models.ForeignKey(Establecimientos,related_name='establecimientoSo', on_delete=models.CASCADE, default=None)
    inspector = models.ForeignKey(Inspector, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.numero_soicitud

    class Meta:
        db_table = 'solicitudinf'  # Custom table name


class SolicitudCons(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateTimeField(auto_now=True)
    numero_soicitud = models.IntegerField(null=False, default=None)
    contribuyente =  models.ForeignKey(Contribuyentes,related_name='solictudesCon', on_delete=models.CASCADE, default=None)
    motivo = models.CharField(max_length=250,null=False,default='ABR')
    inspector = models.ForeignKey(Inspector, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.numero_soicitud

    class Meta:
        db_table = 'solicitudcons'  # Custom table name
