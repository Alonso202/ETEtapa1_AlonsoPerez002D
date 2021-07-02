from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class proveedor(models.Model):
    NumeroIden=models.CharField(max_length=30,primary_key=True,verbose_name='Nombre Identificación')
    Fotografia=models.ImageField
    NombreCompleto=models.CharField(max_length=30,verbose_name='Nombre del Proveedor',validators=[MaxValueValidator(999999999)])
    Telefono=models.PositiveIntegerField( verbose_name='Numero Telefonico')
    direccion=models.CharField (max_length=40,verbose_name='Dirección Proveedor')
    email=models.EmailField(max_length=50,verbose_name='Email de proveedor')
    Pais=models.CharField(max_length=30, verbose_name='País del proveedor')
    Pass=models.CharField(max_length=10, verbose_name='Contraseña Proveedor')
    TipMoneda=models.BooleanField
    def __str__(self):
        return(self.NumeroIden)