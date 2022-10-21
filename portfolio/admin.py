from django.contrib import admin
from .models import Project
# Register your models here.



#clase para extender las funcionalidades del admin
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')  # se le pasan los campos que se desean mostrar solo como lectura 
    
    
admin.site.register(Project,ProjectAdmin) #se pasa la configuracion extendida al admin