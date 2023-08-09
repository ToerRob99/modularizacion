from django.urls import path
from . import views

urlpatterns = [
    path('', views.queris, name='prueba')
]