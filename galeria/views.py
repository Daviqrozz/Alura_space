from django.shortcuts import render,get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografia = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html',{"dados":fotografia})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})

def buscar(request):
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'].upper()
        if nome_a_buscar: 
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)
    return render (request, "galeria/buscar.html", {"dados": fotografia})