from django.urls import path

from . import views

app_name = 'producto'

urlpatterns = [
    path("", views.index, name="index"),
    #path("productocategoria/list/", views.productocategoria_list, name="productocategoria_list"),
    # Para llamar al path desde la clase ProductocategoriaList tenemos que llamar a la clase y usar
    # as_view()  
    path("productocategoria/list/", views.ProductocategoriaList.as_view(), name="productocategoria_list"),
]
