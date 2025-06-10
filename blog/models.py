from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class MonsterHigh(models.Model):
    Muñeca=models.CharField(max_length=300)
    Nombre_modelo=models.CharField(max_length=200)
    Descripcion=models.TextField()
    Fecha_salida=models.DateTimeField(blank=True, null=True)
    Precio_actual=models.CharField(max_length=150)
    Fecha_publicacion= models.DateTimeField(default=timezone.now)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.Muñeca
    
