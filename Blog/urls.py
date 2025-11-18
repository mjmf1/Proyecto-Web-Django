from django.urls import path
from . import views

app_name = 'blog'   # ← IMPORTANTE

urlpatterns = [
    path('', views.blog, name='home'),
]
