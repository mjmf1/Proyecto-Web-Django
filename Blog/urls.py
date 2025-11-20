from django.urls import path
from . import views

app_name = 'blog'   # ← IMPORTANTE

urlpatterns = [
    path('', views.blog, name='home'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]
