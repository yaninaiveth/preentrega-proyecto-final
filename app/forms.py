from django import forms
from platformdirs import user_cache_dir
from .models import Producto,Contacto

# importar para crear formulario de registro de Usuario (VERSION FINAL - AGREGAR!!!!!!)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form de Producto
class ProductCreateForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('articulo','seccion','descripcion','precio_unitario','imagen')

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Form de Contacto
class ContactCreateForms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','email','telefono','asunto','mensaje')

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# FORMULARIO CREADO PARA REGISTRO DE USUARIO
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# FORMULARIO CREADO PARA EDICION DE USUARIO
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']