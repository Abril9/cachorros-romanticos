 python3 manage.py check aplicacion (o el nombre de la aplicacion, chequea si hay inconveientes)


=========================
https://www.youtube.com/watch?v=ezIj71CX944

django-admin startproject perrosromanticos
cd perrosromanticos
python3 manage.py runserver

ir a la url y chequear: The install worked successfully! Congratulations!

crt+c para cerrar 
----------------------------------------------------
python3 manage.py startapp libreria --creo la aplicacion libreria 
agrega la aplicacion libreria en settings.py INSTALLED_APPS=[
    "libreria"
]

---
libreria views.py creo la vista
agrego la url a urls.py de libreria
agrego la url a urls.py de perros romanticos

ya puedo visualizar

---
creo la carpeta templates, de acuerdo a su configuracion django va a ir automaticamente ahi a buscar los templates



