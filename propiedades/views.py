from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
def inmobiliaria(request):
    items_casas = casa.objects.all()
    items_departamentos = departameto.objects.all()
    context = {
        'items_casas': items_casas,
        'items_departamentos': items_departamentos,
    }
    return render(request, 'index.html', context)
def depa(request):
    items_departamentos = departameto.objects.all()
    context = {
        'items_departamentos': items_departamentos,
    }
    return render(request, 'departamentos.html', context)

def nuevacasa(request):
    if request.method ==  "POST":
        form = FormCasa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propiedades:inmobiliaria')
    else:
        form = FormCasa()
        return render(request, 'propiedad/nueva_casa.html', {'form': form})
def nuevodepa(request):
    if request.method ==  "POST":
        form = FormDepa(request.POST)

        if form.is_valid():
            form.save()
            return redirect('propiedades:inmobiliaria')
    else:
        form = FormDepa()
        return render(request, 'propiedad/nuevo_depa.html', {'form': form})

def editarcasa(request, item_id):
    item = casa.objects.get(pk=item_id)
    if request.method == "POST":
        form = FormCasa(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('propiedades:inmobiliaria')
    else:
        form = FormCasa(instance=item)

        return render(request, 'propiedad/editar_casa.html', {'form': form})

def editardepa(request, item_id):
    item = departameto.objects.get(pk=item_id)
    if request.method == "POST":
        form = FormDepa(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('propiedades:depa')
    else:
        form = FormDepa(instance=item)

        return render(request, 'propiedad/editar_depa.html', {'form': form})

def eliminarcasa(request, item_id):

    casa.objects.filter(pk=item_id).delete()

    items = casa.objects.all()

    context = {
        'items': items,
    }

    return redirect('propiedades:inmobiliaria')

def eliminardepa(request, item_id):

    departameto.objects.filter(pk=item_id).delete()

    items = departameto.objects.all()

    context = {
        'items': items,
    }

    return redirect('propiedades:depa')

