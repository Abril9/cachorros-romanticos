"""perrosromanticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings ##importo el archivo de configraciones para recuperar mmis URL definidas
from django.contrib.staticfiles.urls import static

from perrosromanticos.settings import MEDIA_ROOT, MEDIA_URL #importo la ruta estatica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')), #modifico las urls del sistema para incluir las de la aplicacion
]+static(settings.MEDIA_URL, document_root = MEDIA_ROOT)
