#rutas que maneja el framework, acá defino las urls propias de la aplicación 

from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'), #cuando el usuario acceda a la raiz, entra a inicio y se muestra eso
   
    path('administracion', views.administracion, name='administracion'),
    path('listadoUsuarios', views.usuarios, name='listadoUsuarios'),
   
    path('nosotros', views.usuario_nosotros, name='nosotros'),
    path('crearUsuario', views.usuario_crear, name='crearUsuario'),
    path('editarUsuario', views.usuario_editar, name='editarUsuario'),
    path('iniciarSesion', views.usuario_iniciarSesion, name='iniciarSesion'),
    path('registrarme', views.usuario_registrarme, name='registrarme'), 
    
    path('registrarmeArtista', views.artista_registrarme, name='registrarme'),

    path('miColeccion', views.coleccion_miColeccion, name='miColeccion'),

    path('objetoArtistico', views.coleccion_verObjetoArtistico, name='verObjetoArtistico'),
    path('objetoArtistico/<str:codImagen>', views.coleccion_verObjetoArtistico, name='verObjetoArtistico'),

]