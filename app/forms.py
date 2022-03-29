from django import forms
from .models import Producto,Contacto

# Form de Producto
class ProductCreateForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('articulo','seccion','descripcion','precio_unitario')

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Form de Contacto
class ContactCreateForms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','email','telefono','asunto','mensaje')

#------------------------------------------------------------------------------------------------------------------------------------------------------------