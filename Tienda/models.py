from django.db import models

class Categoria(models.Model):
    nombre = models.CharField("Nombre de la categoría", max_length=100, unique=True)
    descripcion = models.TextField("Descripción", blank=True)
    slug = models.SlugField("Slug", max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name="productos",
        verbose_name="Categoría"
    )
    nombre = models.CharField("Nombre del producto", max_length=200)
    descripcion = models.TextField("Descripción")
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Stock disponible")
    imagen = models.ImageField("Imagen del producto", upload_to="Tienda/", blank=True, null=True)
    slug = models.SlugField("Slug", max_length=200, unique=True)
    creado = models.DateTimeField("Fecha de creación", auto_now_add=True)
    actualizado = models.DateTimeField("Última actualización", auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
