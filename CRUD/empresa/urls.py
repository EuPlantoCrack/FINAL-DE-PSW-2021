from unicodedata import name
from xml.etree.ElementInclude import include
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'), 
    path('excluir/<int:empresa_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:empresa_id>/', views.editar, name='editar'),
]