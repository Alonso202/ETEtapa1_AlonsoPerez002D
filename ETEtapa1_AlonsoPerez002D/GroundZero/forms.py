from django import forms
from django.forms import ModelForm, fields,widgets
from .models import proveedor


class ProvForm(ModelForm):
    class Meta:
        model = proveedor
        fields = '__all__'   

