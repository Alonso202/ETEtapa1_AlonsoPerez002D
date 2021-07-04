from django.shortcuts import render,redirect
from .models import proveedor
from .forms import ProvForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html' )
def form_reg_prov(request):
    if request.method == 'POST':
        proveedor_form = ProvForm(data=request.POST, files=request.FILES)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('index')
        else:
            proveedor_form=ProvForm()
        return render(request,'GroundZero/form_reg_prov.html',{'proveedor_form':proveedor_form})
def listado(request):
    proveedores= proveedor.objects.all()
    data={
        'proveedores': proveedores
    }
    return render(request,'GroundZero/listado.html',data)
    




 