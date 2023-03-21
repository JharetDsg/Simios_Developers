from django.contrib import admin
from django.urls import path
from KJPL.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contacto', inicio),
]
