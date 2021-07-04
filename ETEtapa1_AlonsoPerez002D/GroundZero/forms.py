from django import forms
from django.forms import ModelForm, fields,widgets
from .models import proveedor

class ProvForm(ModelForm):
    class Meta:
        model = proveedor
        fields = ['NombreCompleto','email','direccion','Pass','NumeroIden','Fotografia','Telefono','Pais','TipMoneda']
       
        widgets= {
            'NombreCompleto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre Completo',
                    'id':'NombreCompleto'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electronico',
                    'id':'email'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Dirección',
                    'id':'direccion'
                }
            ),
            'pass':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contraseña',
                    'id':'pass'
                }
            ),
            'NumeroIden':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de Identificación',
                    'id':'NumeroIden'
                }
            ),
            'Telefono':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de identificación',
                    'id':'telefono'
                }
            ),
            'pais':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de identificación',
                    'id':'pais'
                }
            ),
            'Fotografia':forms.ClearableFileInput(),
            'TipMoneda':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Tipo Moneda',
                    'id':'TipMoneda'
                }
            ),
        }
