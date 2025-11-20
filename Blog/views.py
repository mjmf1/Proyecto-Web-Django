from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria
from .models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.all().order_by('-created_at')  
    return render(request, "blog/blog.html", {'posts': posts})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    return render(request, "blog/categoria.html", {
        "categoria": categoria,
        "posts": posts,
    })


