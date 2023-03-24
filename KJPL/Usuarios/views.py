from django.shortcuts import render
from Usuarios.models import Usuarios

# Create your views here.
def CrearUsuario(request):
    if request.method == 'POST':
        Dni = request.POST['dni']
        APaterno = request.POST['aPaterno']
        AMaterno = request.POST['aMaterno']
        Nombres = request.POST['nombre']
        FNacimiento = request.POST['fNacimiento']
        Sexo = request.POST['sexo']
        TUsuario = request.POST['tUsuario']

        librito = Usuarios(dni=Dni, aPaterno=APaterno, aMaterno=AMaterno, nombres=Nombres, fNacimiento=FNacimiento, sexo=Sexo, tUsuario=TUsuario)
        librito.save()

        return render(request, "crearUsuario.html", {"dni": Dni})
    return render(request, "crearUsuario.html")

