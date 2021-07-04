from django.db import models

from phone_field import PhoneField

# Create your models here.
opciones_consultas = [
    [0, "Dolar"],
    [1, "Peso Chileno"]
]         
class proveedor(models.Model):
    NumeroIden=models.CharField(max_length=30,primary_key=True,verbose_name='Numero Identificación')
    Fotografia=models.ImageField(upload_to="proveedores",null=True)
    NombreCompleto=models.CharField(max_length=30,verbose_name='Nombre del Proveedor')
    Telefono= PhoneField(blank=True, help_text='Numero de Contacto proveedor')
    direccion=models.CharField (max_length=40,verbose_name='Dirección Proveedor')
    email=models.EmailField(max_length=50,verbose_name='Email de proveedor')
    Pais=models.CharField(max_length=30, verbose_name='País del proveedor')
    Pass=models.CharField(max_length=10, verbose_name='Contraseña Proveedor')
    TipMoneda=models.IntegerField(choices=opciones_consultas)  
    def __str__(self):
        return(self.NumeroIden)