from django.db import models

# Create your models here.

class Cantones (models.Model):
    id_provincia=models.AutoField(primary_key=True)
    codigo=models.IntegerField(null=False)
    nombre=models.CharField(max_length=70, null = False)
    latitud=models.DecimalField(max_digits=32, decimal_places=16, null = False)
    longitud=models.DecimalField(max_digits=32, decimal_places=16, null = False)
    descripcion=models.CharField(max_length=300, null = False)
    imagen=models.ImageField(verbose_name="Imagen", upload_to="cantones")