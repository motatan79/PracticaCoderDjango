from django.urls import path

from . import views

app_name = 'producto'

urlpatterns = [
    path("", views.index, name="index"),
    #path("productocategoria/list/", views.productocategoria_list, name="productocategoria_list"),
    # Para llamar al path desde la clase ProductocategoriaList tenemos que llamar a la clase y usar
    # as_view()  
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    # Detail necesita un pk de la base de datos para hacer la consulta
    path("productocategoria/detail/<int:pk>/", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    # path("productocategoria/update/<int:pk>/", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("productocategoria/update/<int:pk>/", views.productocategoria_update, name="productocategoria_update"),
    #path("productocategoria/delete/<int:pk>/", views.ProductocategoriaDelete.as_view(), name="productocategoria_delete"),
    path("productocategoria/delete/<int:pk>/", views.productocategoria_delete, name="productocategoria_delete"),
]
