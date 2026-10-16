from django.shortcuts import render, get_object_or_404
from .models import Evento, Local

def index(request):
    categoria_id = request.GET.get("categoria")

    if categoria_id:
        eventos = Evento.objects.filter(categoria__id = categoria_id)
    
    else:
        eventos = Evento.objects.all()

    context = {
        "eventos": eventos
    }

    return render(request, "biblioteca/index.html", context)

def detalhe_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)

    context = {
        "evento": evento
    }

    return render(request, "biblioteca/detalhe_evento.html", context)

def local(request, id):
    local = get_object_or_404(Local, pk=id)

    context = {
        "local": local
    }

    return render(request, "biblioteca/local.html", context)