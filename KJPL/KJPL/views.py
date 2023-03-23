from django.http import HttpResponse
from django.shortcuts import render

# Request: Cuando requiero parametros en la vista desde la plantilla (Forms)
#           implementa por defecto los token CSRF - Cross Site Scripting
# Response: Cuando enviamos datos de la vista a la plantilla

def index(request):
    return render(request,"index.html")

def menu(request):
    return render(request,"main.html")

