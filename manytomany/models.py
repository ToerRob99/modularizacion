from django.db import models

class Publicacion(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.title}'


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publicaciones = models.ManyToManyField(Publicacion,)

    def __str__(self) -> str:
        return f'{self.headline}'