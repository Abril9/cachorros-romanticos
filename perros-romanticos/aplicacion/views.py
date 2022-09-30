from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ArtistaForm, UsuarioForm

#para obtener la informacion de la base de datos debo importar el model
from .models  import Usuario, imagen


# Create your views here. 
"""
def inicio(request):
    return HttpResponse("<h1> Bienvenide Perri </h1>")
"""

#    .  .   Generales   .   .   .

def inicio(request):
    return render(request, 'inicio.html')    



#    .  .   Administracion   .   .   .

def administracion(request):
    return render(request, 'administracion/administracion.html')    

def usuarios(request):
    usuarios = Usuario.objects.all()
    print(usuarios)
    return render(request, 'administracion/listadoUsuarios.html',{'cUsuarios': usuarios})    




#    .  .   del Usuario   .   .  .
def usuario_iniciarSesion(request):
    return render(request, 'usuarios/iniciarSesion.html')    


#TODO cambiar esto a coleccionista, pq un usuario nunca se registra
#eso implica cambiar el nombre de la carpeta usuario D: 
#NOTA MENTAL(?) Primero hago que ande para registar artistasss y despues migro esto
def usuario_registrarme(request):
    #al pegarle a registrarme le envio tambien un formulario como post mediante
    #el objeto formulario
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/')
    return render(request, 'usuarios/registrarme.html', {'formulario': formulario})    


def artista_registrarme(request):
    #al pegarle a registrarme le envio tambien un formulario como post mediante
    #el objeto formulario
    formulario = ArtistaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/')
    return render(request, 'artistas/registrarme.html', {'formulario': formulario})    


def usuario_nosotros(request):
    return render(request, 'usuarios/nosotros.html')

def usuario_crear(request):
    return render(request, 'usuarios/crear.html')

def usuario_editar(request):
    return render(request, 'usuarios/editar.html')



#    .  .   de la Coleccion   .   .  .

def coleccion_miColeccion(request):
    imagenes  = imagen.objects.all()
    print(imagenes)
    return render(request, 'coleccion/miColeccion.html',{'imagenes': imagenes})

def coleccion_verObjetoArtistico(request,codImagen):
    return render(request, 'coleccion/verObjetoArtistico.html', {'codImagen': codImagen})