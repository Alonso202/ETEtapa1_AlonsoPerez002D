from django.shortcuts import render,redirect
<<<<<<< HEAD

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html' )
=======
from .models import usuario
from .forms import UsuarioForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def galeria(request):
    return render(request,'Galeria.html')
>>>>>>> 3ea42586a01dc0982fcddc3dbb38bfda3ef7ac8b

def login_registro(request):
    if request.method=='POST': 
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()    #save() reemplaza al insert
            return redirect('index')
    else: 
        usuario_form=UsuarioForm()
    return render(request, 'core/login_registro.html', 
    {'usuario_form':usuario_form})



<<<<<<< HEAD
=======

>>>>>>> 3ea42586a01dc0982fcddc3dbb38bfda3ef7ac8b
 