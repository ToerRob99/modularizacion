from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date


def create(request):
    """
    Funcion:
    """
    rep = Reporter(
        first_name='Daniel', last_name='andres',
        email='danila@example.com'
        )
    rep.save()

    art1 = Article(
        headline='loream ipsum dolot', pub_date=date(2022,5,5),
        reporter=rep
        )
    art1.save()

    art2 = Article(
        headline='lo que sea para ', pub_date=date(2022,3,8),
        reporter=rep
        )
    art2.save()

    art3 = Article(
        headline='aqui un texto de ejemplo', pub_date=date(2022,8,11),
        reporter=rep
        )
    art3.save()

    result = rep.article_set.count()
    #result = rep.article_set.filter(headline='loream ipsum dolot')
    #result = rep.article_set.all()
    #result = art1.reporter.first_name

    return HttpResponse(result)
