from django.urls import path
<<<<<<< HEAD
from .views import home,index
=======
from .views import index,galeria,login_registro
>>>>>>> 3ea42586a01dc0982fcddc3dbb38bfda3ef7ac8b


urlpatterns = [
    path ('', index, name="index"),
<<<<<<< HEAD
    path('home',home,name="home")
=======
    path('galeria',galeria, name="galeria"),
    path('login_registro',login_registro, name="login_registro")
>>>>>>> 3ea42586a01dc0982fcddc3dbb38bfda3ef7ac8b
]