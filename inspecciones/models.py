from django.db import models

class Usuario(models.Model):
   
    i801_codigo  = models.CharField(max_length=6,primary_key=True,null=False)
    i801_nombre = models.CharField(max_length=50,null=False)
    i801_clave  = models.CharField(max_length=10,null=False)
    i801_clase = models.CharField(max_length=3,null=False)
    i801_responsable = models.CharField(max_length=3,null=False)
    i801_activo= models.CharField(max_length=1,null=False)

    def __str__(self):
        return self.i801_codigo


        

    class Meta:
        db_table = 'i801'  # Custom table name

