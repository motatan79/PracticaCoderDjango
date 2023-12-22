from django.shortcuts import render
from .models import Cliente


# Create your views here.
def index(request):
    # Trae todos los clientes en la base de datos
    clientes = Cliente.objects.all()
    return render(request, "cliente/index.html", {"clientes" : clientes})
    