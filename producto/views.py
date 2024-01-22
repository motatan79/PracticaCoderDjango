from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *

# Create your views here.
def index(request):
    return render(request, "producto/index.html")

# lista basada en funciones
# def productocategoria_list(request):
#     objects = ProductoCategoria.objects.all()
#     context = {"object_list": objects}
#     return render(request, "producto/productocategoria_list.html", context)
    
# Listas basadas en clases 

class ProductocategoriaList(ListView):
    model = ProductoCategoria
    # Django sabe a que vista es la lista porque es el nombre de la clase que contiene el url
    # template_name = "producto/productocategoria_list.html"
    # context_object_name = "object_list"
    
    # Para obtener la consulta desde la base de datos
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            return self.model.objects.filter(
                nombre__icontains = self.request.GET.get("consulta")
            )
        return self.model.objects.all()