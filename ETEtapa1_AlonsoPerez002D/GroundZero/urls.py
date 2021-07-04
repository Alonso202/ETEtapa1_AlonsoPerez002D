from django.urls import path
from .views import home,index,form_reg_prov ,listado



urlpatterns = [
    path ('', index, name="index"),
    path('home',home,name="home"),
    path('form_reg_prov',form_reg_prov,name="form_reg_prov"),
    path('listado',listado,name="listado")
]