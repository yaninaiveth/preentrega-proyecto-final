from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForms
from .models import Post,OrdenCompra
from django.urls import reverse_lazy

# Vista de Clase que lista los posts 
class BlogListView(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request,'blog_list.html',context)


# Vista de clase de crea permite crear un nuevo post
class BlogCreateView(View):
    def get(self,request,*args,**kwargs):
        #parte creada para llamar el contenido del form creado en forms.py (donde generamos titulo y conenido de blog)
        form = PostCreateForms()
        context={
            'form':form    
        }
        return render(request,'blog_create.html',context)
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            form = PostCreateForms(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect('blog:home')

        context = {
        }
        return render(request,'blog_create.html',context)


class BlogDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        post = get_object_or_404(Post,pk=pk)
        context = {
            'post':post
        }
        return render(request,'blog_detail.html',context)


# Vista de clase que permite modificar (update) nuestro post
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})

# Vista de clase que nos permite eliminar un post
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')
