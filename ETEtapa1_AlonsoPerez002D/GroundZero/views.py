from django.shortcuts import render,redirect
from .models import proveedor
from .forms import ProvForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html' )
def form_reg_prov(request):

    data = {
        'form': ProvForm()
    }

    if request.method == 'POST':
        formulario = ProvForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data['form'] = formulario

    
    return render(request, 'GroundZero/form_reg_prov.html', data)

def listado(request):
    proveedores= proveedor.objects.all()
    data={
        'proveedores': proveedores
    }
    return render(request,'GroundZero/listado.html',data)
    




 