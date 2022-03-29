from urllib import request
from django.shortcuts import render

# vista de funcón (def) - Vista de Inicio de nuestro página/blog
def HomeView(request):
        context = {

        }
        return render(request,'index.html',context)