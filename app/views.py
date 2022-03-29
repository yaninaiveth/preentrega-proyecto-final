from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView,ListView
from .forms import ProductCreateForms,ContactCreateForms
from .models import Cliente,Producto,Pedido,Contacto
from django.urls import reverse_lazy


## VISTAS DE CLIENTE
# Vista de Clase que lista los clientes
class ClientListView(ListView):
    def get(self,request,*args,**kwargs):
        clientes = Cliente.objects.all()
        context = {
            'clientes':clientes
        }
        return render(request,'clientes_list.html',context)

#----------------------------------------------------------------------------------------------

## VISTA DE PRODUCTO
# Vista de Clase que lista los productos
class ProductListView(ListView):
    def get(self,request,*args,**kwargs):
        productos = Producto.objects.all()
        context = {
            'productos':productos
        }
        return render(request,'productos_list.html',context)


# Vista para realizar búsqueda de productos (por articulo)
def SearchProductView(request):
        context = {
        }
        return render(request,'buscar_producto.html',context)


# Vista para mostar productos buscados (por articulo)
def ToFindProductView(request):
        if request.GET["articulo"]:
            articulo = request.GET["articulo"]
            productos = Producto.objects.filter(articulo__icontains=articulo)
            context = {
                'productos': productos,
                'query': articulo
            }
            return render(request,'resultado_buscar_producto.html',context)

        else:
            mensaje = "Por favor introduce un artículo"
        return HttpResponse(mensaje)


# Vista de clase - permite crear un nuevo Producto
class ProductCreateView(View):
    def get(self,request,*args,**kwargs):
        #parte creada para llamar el contenido del form creado en forms.py (donde generamos titulo y conenido de blog)
        form = ProductCreateForms()
        context={
            'form':form    
        }
        return render(request,'crear_producto.html',context)
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            form = ProductCreateForms(request.POST)
            if form.is_valid():
                articulo = form.cleaned_data.get('articulo')
                seccion = form.cleaned_data.get('seccion')
                descripcion = form.cleaned_data.get('descripcion')
                precio_unitario = form.cleaned_data.get('precio_unitario')

                p, created = Producto.objects.get_or_create(articulo=articulo,seccion=seccion,descripcion=descripcion,precio_unitario=precio_unitario)
                p.save()
                return redirect('app:productos')

        context = {
        }
        return render(request,'crear_producto.html',context)


# Vista de clase que permite modificar (update) nuestro producto
class ProductUpdateView(UpdateView):
    model = Producto
    fields = ['articulo','seccion','descripcion','precio_unitario']
    template_name = 'modifcar_producto.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('app:productos')
        

# Vista de clase que nos permite eliminar un producto
class ProductDeleteView(DeleteView):
    model = Producto
    template_name = 'borrar_producto.html'
    success_url = reverse_lazy('app:productos')

#----------------------------------------------------------------------------------------------

## VISTAS DE CONTACTO
# Vista de clase - permite crear un nuevo Producto
class ContactCreateView(View):
    def get(self,request,*args,**kwargs):
        #parte creada para llamar el contenido del form creado en forms.py (donde generamos titulo y conenido de blog)
        form = ContactCreateForms()
        context={
            'form':form    
        }
        return render(request,'contacto.html',context)
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            form = ContactCreateForms(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                email = form.cleaned_data.get('email')
                telefono = form.cleaned_data.get('telefono')
                asunto = form.cleaned_data.get('asunto')
                mensaje = form.cleaned_data.get('mensaje')

                c, created = Contacto.objects.get_or_create(nombre=nombre,email=email,telefono=telefono,asunto=asunto,mensaje=mensaje)
                c.save()
                return redirect('app:contacto')

        context = {
        }
        return render(request,'contacto.html',context)

