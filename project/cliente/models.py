from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = 'Países'
        
    
class Cliente(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    nacimiento = models.DateField(null= True, blank = True)
    emailid = models.CharField(max_length=100)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    pais_origen_id = models.ForeignKey(Pais, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = 'País de origen')
    
    def __str__(self) -> str:
        return f'{self.apellido}, {self.nombre}'