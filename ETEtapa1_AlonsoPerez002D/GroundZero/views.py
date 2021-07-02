from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html' )
def form_reg_prov(request):
    return render(request,'GroundZero/form_reg_prov.html')




 