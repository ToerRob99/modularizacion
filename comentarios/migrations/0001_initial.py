# Generated by Django 4.2.4 on 2023-08-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre del comentario')),
                ('score', models.IntegerField(blank=True, default=2, null=True, verbose_name='Numero de comentario')),
                ('comment', models.TextField(max_length=1000, null=True)),
                ('date', models.DateField(null=True)),
                ('signature', models.TextField(null=True, verbose_name='Firma')),
            ],
        ),
    ]
