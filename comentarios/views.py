from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario

def test(request):
    return HttpResponse(
        "Funciona correctamente"
    )


def create(request):
    # comment = Comentario(name="juan", score=5, comment="este es un comentario")
    # comment.save()
    comment = Comentario.objects.get_or_create(name="pedro", score=8)
    return HttpResponse("En esta ruta prueba controlador para guardar")


def delete(request):
    # comment = Comentario.objects.get(id=1)
    # comment.delete()
    Comentario.objects.filter(id=2).delete()
    return HttpResponse("En esta ruta prueba la eliminacion de un registro")