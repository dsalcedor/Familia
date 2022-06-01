from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from miembros.forms import FamiliarForm

from miembros.models import Familiar

# Create your views here.

def index(request):
    familiar = Familiar.objects.all()
    template = 'miembros/index.html'
    context = {
        'familiar':familiar,
    }
    return render(request, template, context)

def agregar(request):
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            edad = form.cleaned_data['edad']
            Familiar(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, edad=edad).save()

            return HttpResponseRedirect('/familia/')
    elif request.method =='GET':
        form = FamiliarForm()
    else:
        return HttpResponseBadRequest('No hay metodo para esta request')
    
    return render(request, 'miembros/form_carga.html', {'form': form})

def borrar(request, identificador):
    
    if request.method == "GET":
        persona = Familiar.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

