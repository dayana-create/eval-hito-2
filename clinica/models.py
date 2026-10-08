from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    codigo_clasificacion = models.CharField(max_length=10, unique=True) 
    descripcion = models.TextField(blank=True, null=True)
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.nombre} ({self.codigo_clasificacion})'
    

class PacienteMascota(models.Model):
    nombre_mascota = models.CharField(max_length=100)
    nombre_dueno = models.CharField(max_length=150)
    numero_chip = models.CharField(max_length=15, unique=True) 
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    edad_anios = models.IntegerField()
    en_tratamiento = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='pacientes')
    
    def __str__(self):
        return f'{self.especie},{self.nombre_mascota},{self.numero_chip},{self.peso_kg},{self.edad_anios},{self.en_tratamiento},{self.fecha_registro})'
    
    