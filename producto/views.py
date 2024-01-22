from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, "producto/index.html")

# lista basada en funciones
# def productocategoria_list(request):
#     objects = ProductoCategoria.objects.all()
#     context = {"object_list": objects}
#     return render(request, "producto/productocategoria_list.html", context)
    
# Listas basadas en clases 

# Para obtener una lista 
class ProductoCategoriaList(ListView):
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
 
 # Para crear una lista    
class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    forms_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    fields = "__all__"


# Para ver en detalle 
class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
    # template_name = "producto/productocategoria_detail.html"

# Ahpra con funciones 
def productocategoria_detail(request, pk):
    consulta = ProductoCategoria.objects.get(id=pk)
    return render(request, "producto/productocategoria_detail.html", {"object": consulta})




# Para Actualizar    
class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    fields = "__all__"
    
# PAra hacer un update de productocategoria

def productocategoria_update(request, pk):
    consulta = ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        form = ProductoCategoriaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("producto:productocategoria_list")
    else:
        form = ProductoCategoriaForm(instance=consulta)
    return render(request, "producto/productocategoria_update.html", {"form": form})    
    

class ProductocategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    fields = "__all__"
    
# Usando funciones 
def productocategoria_delete(request, pk):
    consulta = ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("producto:productocategoria_list")
    return render(request, "producto/productocategoria_confirm_delete.html", {"object": consulta})


