from django.contrib import admin
from Usuarios.models import Usuarios

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('dni', 'apellidoPaterno', 'apellidoMaterno','nombres','fechaNacimiento','sexo','tipoUsuario')

admin.site.register(Usuarios, UsuarioAdmin)