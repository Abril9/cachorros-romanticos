from dataclasses import field
from django import forms
from .models import Usuario, artista, coleccionista


#Declaro el formulario para creacion de usuarios 
#TODO cambiar a coleccionista

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['pais_alias'] 

#Declaro el formulario para creacion de coleccionistas 
class ArtistaForm(forms.ModelForm):
    class Meta:
        model = artista
        exclude = ['pais_alias'] 