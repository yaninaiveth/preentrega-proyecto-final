from django import forms
from .models import Post

# Form de Posteo (Blog)
class PostCreateForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')

# Form de clientes (Market)
class Cliente(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    direccion= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono= forms.CharField(max_length=30)

# Form Orden de Compra (Market)
class OrdenDeCompra(forms.Form):
    sabor = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    precio_unitario = forms.IntegerField()

# Form Valoraciones (Market)
class Valoraciones(forms.Form):
    valoracion = forms.TextInput()
    puntaje = forms.IntegerField()
