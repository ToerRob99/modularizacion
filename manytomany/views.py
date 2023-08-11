from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion, Article


def create(request):
    art1 = Article(headline='Articulo primero')
    art1.save()

    art2 = Article(headline='Articulo segundo')
    art2.save()

    art3 = Article(headline='Articulo tercero')
    art3.save()


    pub1 = Publicacion(title='Publicacion primera')
    pub1.save()
    pub2 = Publicacion(title='publicacion segunda')
    pub2.save()
    pub3 = Publicacion(title='Publicacion tercera')
    pub3.save()
    pub4 = Publicacion(title='Publicacion cuarta')
    pub4.save()
    pub5 = Publicacion(title='Publicacion quinta')
    pub5.save()
    pub6 = Publicacion(title='Publicacion sexta')
    pub6.save()
    pub7 = Publicacion(title='Publicacion septima')
    pub7.save()

    art1.publicaciones.add(pub1)
    art1.publicaciones.add(pub2)
    art1.publicaciones.add(pub3)
    art2.publicaciones.add(pub4)
    art2.publicaciones.add(pub5)
    art3.publicaciones.add(pub6)
    art3.publicaciones.add(pub7)

    #art1.publicaciones.remove(pub1)
    #pub1 = Publicacion.objects.get(id=1)
    result = pub1.article_set.all()

    return HttpResponse(result)
