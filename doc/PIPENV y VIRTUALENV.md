https://code.tutsplus.com/es/tutorials/understanding-virtual-environments-in-python--cms-28272


PIPENV y VIRTUALENV 
** ¿Qué es un Entorno Virtual? Un entorno virtual es una herramienta para mantener espacio separado para un proyecto con sus dependencias y librerías en un lugar. Este entorno es específico para el proyecto particular y no interfiere con las dependencias de otros proyectos.
Por ejemplo, puedes trabajar en un proyecto X que está usando la versión 1.0 de la librería Z y también mantener al proyecto Y que está usando la versión 2.0 de la librería Z.

** ¿Cómo Funcionan los Entornos Virtuales? La herramienta de entorno virtual crea una carpeta dentro del directorio del proyecto. Por defecto, la carpeta es llamada venv, pero puedes renombrarla también. Mantiene archivos Python y pip ejecutables dentro de la carpeta de entorno virtual. Cuando el entorno virtual es activado, los paquetes instalados después de eso son instalados dentro de la carpeta de entorno virtual de proyecto específico. 

** Comenzando Con VirtualEnv
Primero, asegúrate de que tienes pip instalado en tu sistema. Puedes instalar pip usando el siguiente comando:
	
sudo apt-get install pip python-dev build-essential

Usando pip, instala la herramienta de entorno virtual.

pip install virtualenv

Para comenzar usando virtualenv, necesitas inicializarlo y activarlo. Comencemos creando un nuevo directorio de proyecto Python PythonApp.
	
mkdir PythonApp

Navega al directorio de proyecto PythonApp e inicializa el entorno virtual tecleando el siguiente comando:
	
virtualenv PythonAppVenv

El comando de arriba configurará el entorno virtual par el proyecto PythonApp, mantiene los ejecutables Python y pip dentro de la carpeta de entorno virtual. Cualquier nuevo paquete instalado para el proyecto después de la activación del entorno virtual son colocados dentro de la carpeta de entorno virtual. Aquí está la estructura de la carpeta.


** Setting Up Virtual Environment: para comenzar usando el entorno virtual, necesitas activarlo usando el siguiente comando:
	
source PythonAppVenv/bin/activate

Luego podremos instalar con pip cualquier paquete que necesitemos. l