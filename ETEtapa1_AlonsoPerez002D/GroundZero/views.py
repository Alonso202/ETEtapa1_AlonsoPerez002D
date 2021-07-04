from django.shortcuts import render,redirect,get_object_or_404
from .models import proveedor
from .forms import ProvForm

# Create your views here.
def index(request):
    return render(request,'index.html')
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

def modificar(request, NumeroIden):

    producto = get_object_or_404(proveedor, NumeroIden=NumeroIden)

    data = {
        'form': ProvForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProvForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listado")
        data["form"] = formulario 


    return render(request, 'GroundZero/modificar.html', data)  
def eliminar(request,NumeroIden):
    producto = get_object_or_404(proveedor, NumeroIden=NumeroIden)
    producto.delete()
    return redirect(to="listado")




 