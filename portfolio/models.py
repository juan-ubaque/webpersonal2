from tabnanny import verbose
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField (max_length=200 , verbose_name="Titulo")
    description = models.TextField( verbose_name="Descripcion")
    image = models.ImageField ( verbose_name="Imagen",upload_to="projects") #upload_to le dice en que carpeta guarga los media
    created = models.DateTimeField (auto_now_add=True, verbose_name="Fecha-Creacion")
    updated = models.DateTimeField (auto_now=True,verbose_name="Fecha-Edicion")
    link = models.URLField (blank=True,null=True)
    
    class Meta: 
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos" #nombre en admin en plural
        ordering = ["-created"]  #para ordenar los campos en el admin
    def __str__ (self):
        return self.title