from pathlib import Path
from django.urls import path
from .views import *

# AGERGADO PARA EL LOGOUT
from django.contrib.auth.views import LogoutView



app_name = 'app'

urlpatterns = [
    
    path('clientes/',ClientListView.as_view(),name="clientes"),
    path('productos/',ProductListView.as_view(),name="productos"),
    path('buscar_producto/',SearchProductView,name="buscar_producto"),
    path('producto_buscado/',ToFindProductView,name='producto_buscado'),
    path('crear_producto/',ProductCreateView.as_view(),name="crear_producto"),
    path('contacto/',ContactCreateView.as_view(),name="contacto"),
    path('<int:pk>/modificar/',ProductUpdateView.as_view(),name="modificar_producto"),
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name="borrar_producto"),
    #-------------------------------------------AGREGADOS PARA LA VERSION FINAL----------------------------------------------------------------------------
    path('login',login_request,name="login"),                                   # VISTA QUE SE AGREGA PARA LOGUEARSE A LA WEB!!
    path('registro',register,name="registro"),                                  # VISTA QUE SE AGREGA PARA REGISTRARSE EN LA WEB!!    
    path('logout',LogoutView.as_view(),name="logout"),                          # VISTA QUE SE AGREGA PARA DESLOGUEARSE EN LA WEB!!    
    path('nosotros/',AboutUsView,name="nosotros"),                              # VISTA SOBRE NOSOTROS
    
]

