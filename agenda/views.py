from django.shortcuts import render
from .models import Evento

def index(request):
    eventos = Evento.objects.all()

    context = {
        "eventos": eventos
    }

    return render(request, "biblioteca/index.html", context)

def detalhe_evento(request, id):
    evento = Evento.objects.get(pk=id)

    context = {
        "evento": evento
    }

    return render(request, "biblioteca/detalhe_evento.html", context)