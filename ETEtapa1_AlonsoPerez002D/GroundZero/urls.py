from django.urls import path
from .views import index,form_reg_prov ,listado,modificar,eliminar



urlpatterns = [
    path ('', index, name="index"),
    path('form_reg_prov',form_reg_prov,name="form_reg_prov"),
    path('listado',listado,name="listado"),
    path('modificar/<NumeroIden>/',modificar,name="modificar"),
    path('eliminar/<NumeroIden>/',eliminar,name="eliminar"),
    ]