para cuando no anda nada :)
❯ python3 manage.py migrate --fake aplicacion zero
❯ python3 manage.py migrate  aplicacion 

lo saque de https://stackoverflow.com/questions/35494035/django-migrate-doesnt-create-tables/43677713#43677713
--------
# Connect to your postgres DB
conn = psycopg2.connect("dbname=pr-db-1 user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM my_data")

# Retrieve query results
records = cur.fetchall()
para mas > https://www.neoguias.com/como-conectarse-postgresql-python/


------
sudo nano /etc/postgresql/12/main/
systemctl restart postgresql
❯ psql postgres postgres
https://www.postgresql.org/docs/current/app-psql.html
https://aws.amazon.com/es/blogs/aws-spanish/managing-postgresql-users-and-roles/

-----------------------------------


articulo para instalar postgresql 
https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-18-04-es



Creacion de la bdd con postgresql
sudo nano /etc/postgresql/12/main/pg_hba.conf 
Reinstalar postgres14
poner en trust el metodo de autenticacion para localhost 127.0.0.1
reload del servcio

El localhost tiene la dirección IP 127.0.0.1, la cual hace referencia al servidor en el propio equipo.23
la dirección IP 192.168.1.0 pertenece al bloque de 16 bits de la dirección IP privada.
En la mayoría de los casos, esta dirección IP es utilizada por los routers de banda ancha domésticos como su dirección predeterminada.
nmap -p 5432 -PN Localhost

netstat -na | grep tcp


Conexion a la base de datos
ir a settings.py


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

configuracion de bdd por dfault, se genera una base de datos portatil 

tengo que tener la bdd implemtnada

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'perros_romanticos_db',
        'USER': 'perros_romanticos_owner',
        'PASSWORD' : 'password',
        'HOST':'localhost' #esta es la direccion dnde esta la bdd
        'PORT': '3307' #este apunta a mysql
    }
}


----
Segui el tutorial de https://stackpythonex.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8

basicamente:
en Models.py
from django.db import models
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

  pip install psycopg2-binary
  python manage.py makemigrations
  python manage.py migrate


DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'perrosromanticos_db',
        'USER': 'postgres',
        'PASSWORD' : 'password',
        'HOST':'localhost',
        'PORT': '5432'
    }
}



wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.1/pip/pgadmin4-2.1-py2.py3-none-any.whl



-----
SUPERUSER ADMINISTRADOR QUE USE LA INFORMACION DE LA BDD
❯ phyton3 manage.py createsuperuser
usuario: abril, use mi gmail y la pass es la misma que para las bdd de rectorado :)
luego puedo acceder a la consola de administracion de la base de datos con la url de la app /admin, ingresando la info del loggin
