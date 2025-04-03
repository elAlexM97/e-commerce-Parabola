from django.db import models
from django.urls import reverse

# Modelo para la categoría de productos
class Category(models.Model):
    name = models.CharField(max_length=200)  # Nombre de la categoría
    slug = models.SlugField(max_length=200, unique=True)  # Identificador único en la URL

    class Meta:
        ordering = ['name']  # Ordena las categorías alfabéticamente por nombre
        indexes = [
            models.Index(fields=['name']),  # Agrega un índice para mejorar las búsquedas por nombre
        ]
        verbose_name = 'category'  # Nombre en singular para el panel de administración
        verbose_name_plural = 'categories'  # Nombre en plural para el panel de administración

    def __str__(self):
        return self.name  # Representación en cadena del modelo

    def get_absolute_url(self):
        # Retorna la URL para ver los productos filtrados por categoría
        return reverse('shop:product_list_by_category', args=[self.slug])

# Modelo para los productos en la tienda
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Relación con la categoría
    name = models.CharField(max_length=200)  # Nombre del producto
    slug = models.SlugField(max_length=200)  # Identificador único en la URL
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # Imagen del producto, organizada por fecha
    description = models.TextField(blank=True)  # Descripción del producto (opcional)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto con dos decimales
    available = models.BooleanField(default=True)  # Indica si el producto está disponible para la venta
    created = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación automática
    updated = models.DateTimeField(auto_now=True)  # Fecha y hora de última actualización automática

    class Meta:
        ordering = ['name']  # Ordena los productos alfabéticamente por nombre
        indexes = [
            models.Index(fields=['id', 'slug']),  # Índice para mejorar búsquedas por ID y slug
            models.Index(fields=['name']),  # Índice para optimizar búsquedas por nombre
            models.Index(fields=['-created']),  # Índice para ordenar por fecha de creación de forma descendente
        ]

    def __str__(self):
        return self.name  # Representación en cadena del modelo

    def get_absolute_url(self):
        # Retorna la URL para ver los detalles de un producto específico
        return reverse('shop:product_detail', args=[self.id, self.slug])


    