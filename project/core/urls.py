from django.urls import path
from .views import index

# Para navegar entre las apps (páginas)
app_name = 'core'


urlpatterns = [
    path("", index, name='index'),
]
