from django.shortcuts import render
from Usuarios.models import Usuarios

# Create your views here.
def CrearUsuario(request):
    if request.method == 'POST':
        dni = request.POST['dni']
        APaterno = request.POST['apellidoPaterno']
        AMaterno = request.POST['apellidoMaterno']
        Nombres = request.POST['nombres']
        FNacimiento = request.POST['fechaNacimiento']
        Sexo = request.POST['sexo']
        TUsuario = request.POST['tipoUsuario']

        User = Usuarios(dni=dni, apellidoPaterno=APaterno, apellidoMaterno=AMaterno, nombres=Nombres, fechaNacimiento=FNacimiento, sexo=Sexo, tipoUsuario=TUsuario)
        User.save()

        return render(request, "crearUsuario.html", {"dni": dni})
    return render(request, "crearUsuario.html")

