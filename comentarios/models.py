from django.db import models

class Comentario(models.Model):
    name = models.CharField(
        verbose_name = "Nombre del comentario",
        max_length = 255,
        unique=True
    )
    score = models.IntegerField(
        verbose_name = "Numero de comentario",
        default = 2,
        blank = True,
        null = True,
    )
    comment = models.TextField(
        max_length=1000,
        null=True
    )
    date = models.DateField(
        null = True
    )
    signature = models.TextField(
        verbose_name = "Firma",
        null = True
    )

    def __str__(self) -> str:
        return f'{self.name.title()}'
