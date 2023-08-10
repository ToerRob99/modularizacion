from django.urls import path
from . import views

urlpatterns = [
    path('create2/', views.create, name='create')
]