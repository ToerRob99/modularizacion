from django.shortcuts import render
from .models import Author, Entry

def queris(request):
    #obtener todos los objetos
    authors = Author.objects.all()

    # filtrado por el correo
    filtered = Author.objects.filter(email='zrose@example.org')

    #obteniendo el autor por el id
    author = Author.objects.get(id=1)

    #obtener los 10 primeros
    limits = Author.objects.all()[:10]

    #obtener los 5 elemento saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    #ordenar por email
    orders = Author.objects.all().order_by('email')

    # obtener y filtar por id colocando si es menor o igual 15
    # (__gte mayoy o igual)(__contains contiene)(__exat exacto)
    filtereds = Author.objects.filter(id__lte= 15)

    return render(
        request,
        'post/queris.html',
        {
            'authors': authors,
            'filtered':filtered,
            'author':author,
            'limits':limits,
            'offsets':offsets,
            'orders':orders,
            'filtereds':filtereds,
        }
    )