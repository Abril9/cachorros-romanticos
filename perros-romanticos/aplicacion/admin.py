from curses.ascii import US
from django.contrib import admin

# Register your models here.
# un administrativo tiene que poder administrar la bdd 
# la infromacion que voy a necesitar para ello esta en models asi que lo tengo que importar
# a las tablas ingresadas aqui las voy a poder editar desde la pagina de administrador de la app
from .models import Usuario, artista,administrador,coleccionista,objeto_artisitico, imagen
admin.site.register(Usuario)
admin.site.register(artista)
admin.site.register(administrador)
admin.site.register(coleccionista)
admin.site.register(objeto_artisitico)
admin.site.register(imagen)