from ast import Or
from django.contrib import admin
from .models import Cliente, OrdenCompra, Valoraciones
# Register your models here.

admin.site.register(Cliente) 
admin.site.register(OrdenCompra)
admin.site.register(Valoraciones)