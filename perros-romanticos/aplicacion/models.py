import code
from email.policy import default
from django.db import models
from django.utils import timezone

#CAPTURA LA ESTRUCTURA DE NUESTRA BASE DE DATOS
#luego corro:
#python3 manage.py makemigrations 
#python3 manage.py migrate #para hacer efectivos los cambiossss 

#level 0
class pais(models.Model):
    alias = models.CharField(primary_key=True, max_length=80)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

#level 1
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    usuario = models.CharField(max_length=80, verbose_name='Nombre de usuario')
    imagen = models.ImageField(upload_to='imagenes/', null=False, default='-')
    email = models.EmailField(default='-')
    pais_alias = models.ForeignKey(pais, default='AR', on_delete= models.PROTECT)
#    fecha_alta = models.DateTimeField(default=timezone.get_current_timezone, null=False)

    #funcion analoga a toString(),The __str__ method just tells Django what to
    #print when it needs to print out an instance of the any model

    def __str__(self):
        return self.usuario

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#level 2
class administrador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete= models.PROTECT)
    privilegios = models.IntegerField(default=0)
    
    def __str__(self):
        return self.usuario.usuario

class artista(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)    
    
    def __str__(self):
        return self.usuario.usuario

class coleccionista(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, max_length = 80, on_delete = models.PROTECT)
    coleccion = models.ManyToManyField('objeto_artisitico') #Las comillas son pq se crea despues la tabla de oa
    
    def __str__(self):
        return self.usuario.usuario

#level 3
class objeto_artisitico(models.Model):
    
    IMAGEN = 'IMG'
    VIDEO = 'VID'
    AUDIO = 'AUD'
    OTRO = 'OTRO'
    OA_TIPO = [
        (IMAGEN, 'Imagen'),
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
        (OTRO, 'Otro'),
    ]
    
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(artista, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=1500)
    tipo = models.CharField(max_length=10, choices=OA_TIPO, default = OTRO)
    fecha = models.DateTimeField()
    ref = models.CharField( max_length=500)

    def __str__(self):
        return self.titulo


class imagen(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='imagenes/', null=True)

    def __str__(self):
        return 'imagen: '+ str(self.id)