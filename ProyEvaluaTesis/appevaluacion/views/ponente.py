from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from appevaluacion.models import Alumno
from appevaluacion.forms import *
from django.contrib import messages


@login_required(login_url='login')
def listar_ponentes(request):
    return render(request, "ponente/listar.html")

@login_required(login_url='login')
def listar_ponentes_json(_request):    
    ponente = list(Alumno.objects.values())
    data = {'ponente':ponente}
    return JsonResponse(data)


@login_required(login_url='login')
def crear_ponente(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():       
            form.save()             
            messages.success(request, f'Ponente Creado Exitosamente')
            return redirect('listar_ponentes')
        else:
            messages.error(request, "El formulario contiene errores. Por favor, corrija")
    else:
        form = AlumnosForm()
    return render(request, 'ponente/agregar.html', {'form': form})


@login_required(login_url='login')
def actualizar_ponente(request, id):
    ponente = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        form = AlumnosForm(request.POST, instance=ponente)
        if form.is_valid():
           form.save()
           messages.success(request, f'Poenente actualizado exitosamente.')
           return redirect('listar_ponentes')
        else:
           messages.error(request, "El formulario contiene errores. Por favor, corrija")
    else:
        form = AlumnosForm(instance=ponente)
    return render(request, 'ponente/editar.html', {'form': form})