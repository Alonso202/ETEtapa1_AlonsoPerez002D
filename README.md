# Entrega4

#superuser
admin
alonsin1711


#creación de usuario 
CREATE USER c##GroundZero identified by 1234;
GRANT CONNECT, RESOURCE TO c##GroundZero;
ALTER USER c##GroundZero DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;
#necesario para ocupar pagina
pip install django-phone-field
pip install -r requirements.txt

