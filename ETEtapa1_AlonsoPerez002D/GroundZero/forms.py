from django import forms
from django.forms import ModelForm, fields,widgets
from .models import proveedor

class UsuarioForm(ModelForm):
    class Meta:
        model = proveedor
        fields = ['NomCompleto','email','direccion','contraseña','NumeroIden','Fotografia','Telefono','pais','TipMoneda']
       
        widgets={
            'NomCompleto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre Completo',
                    'id':'NomCompleto'
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
                    'id':'contraseña'
                }
            ),
            'NumeroIden':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Numero de Identificación',
                    'id':'NumId'
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
                    'id':'telefono'
                }
            ),


            
        }


