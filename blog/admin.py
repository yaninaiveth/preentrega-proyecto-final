from django.contrib import admin
from .models import Post,Cliente, OrdenCompra,Valoraciones
# Register your models here.

admin.site.register(Post)
admin.site.register(Cliente) 
admin.site.register(OrdenCompra)
admin.site.register(Valoraciones)