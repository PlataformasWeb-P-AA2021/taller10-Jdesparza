from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py 
from ordenamiento.forms import *

def index(request):
    """
    """
    parroquia = Parroquia.objects.all()

    informacion_template = {'parroquia': parroquia}
    return render(request, 'index.html', informacion_template)

# Generar una vista que liste las parroquias y sus barrios
def listar_Parroquias_Barrios(request):
    """
    """
    parroquia= Parroquia.objects.all()

    informacion_template = {'parroquia': parroquia}
    return render(request, 'listar_Parroquias_Barrios.html', informacion_template)

# Generar una vista que liste los barrios
def listar_Barrios(request):
    """
    """
    barrio= Barrio.objects.all()

    informacion_template = {'barrio': barrio}
    return render(request, 'listar_Barrios.html', informacion_template)

# Generar un formulario que cree una parroquia
def crear_Parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_Parroquia.html', diccionario) 

# Generar un formulario que cree un barrio de una parroquia
def crear_Barrio_Parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crear_Barrio_Parroquia.html', diccionario)  

# Generar un formulario que edite una parroquia
def editar_Parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_Parroquia.html', diccionario) 

# Generar un formulario que edite un barrio
def editar_Barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_Barrio.html', diccionario) 

# Crear Barrio
def crear_Barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_Barrio.html', diccionario) 