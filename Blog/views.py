from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria
from .models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    categorias = Categoria.objects.all()    
    return render(request, "blog/blog.html", {'posts': posts, 'categorias': categorias})

