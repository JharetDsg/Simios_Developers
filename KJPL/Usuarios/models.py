from django.db import models

# Create your models here.
class Usuarios(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M','Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    TipoUsuario = [
        ('Administrador','Administrador'),
        ('Director','Director'),
        ('Docente','Docente'),
        ('Alumno','Alumno'),
        ('Coordinador','Coordinador')
    ]
    
    tipoUsuario = models.CharField(max_length=20, choices=TipoUsuario, default='Administrador')