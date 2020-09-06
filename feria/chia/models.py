from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null = True, blank=True)
    telefono = models.CharField(max_length=50, null = True, blank=True)
    def __str__(self):
        return self.nombre+" "+self.apellido
    
class Articulo(models.Model):
    numero_de_articulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)  
    comprador = models.ForeignKey(Cliente, related_name="articulos",on_delete=models.DO_NOTHING, null = True, blank=True)
    fecha_de_venta = models.DateField( null = True, blank=True)
    def __str__(self):
        return "Articulo N°"+self.numero_de_articulo
    
# Create your models here.
