from django.db import models

# Create your models here.

# Clase cliente (comprador)
class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Apellido: {self.apellido}'

# Clase Piza para venta
class OrdenCompra(models.Model):
    sabor = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    #precio_total = cantidad*precio_unitario

    def __str__(self) -> str:
        return f'OC - Sabor: {self.sabor} | Cant.: {self.cantidad} | P.unit.: ${self.precio_unitario} | Total: ${self.precio_total}'

# Clase Valoraciones (Feedback clientes)
class Valoraciones(models.Model):
    valoracion = models.TextField()
    puntaje = models.IntegerField()

    def __str__(self) -> str:
        return f'Comentario: {self.valoracion} | Puntaje: {self.puntaje}'





