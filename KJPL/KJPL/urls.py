from django.contrib import admin
from django.urls import path
from KJPL.views import index,menu
from Usuarios.views import CrearUsuario


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('menu',menu),
    path('cUser',CrearUsuario),
]
