from django.db import models

# Create your models here.

# Clase cliente (comprador)
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | Dirección: {self.direccion} | email: {self.email} | telefono: {self.telefono}'

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clase Producto
class Producto(models.Model):
    articulo = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio_unitario = models.IntegerField()

    def __str__(self) -> str:
        return f'Artículo: {self.articulo} | Sección: {self.seccion} | P.unit.: ${self.precio_unitario}'

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clase Pedidos
class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clase Contacto (Feedback clientes)
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self) -> str:
        return f'Mensaje - Asunto: {self.asunto} | Mensaje: {self.mensaje}'

#------------------------------------------------------------------------------------------------------------------------------------------------------------
