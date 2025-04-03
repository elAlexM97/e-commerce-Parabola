from django.contrib import admin
from .models import Category, Product

@admin.register(Category)   # Registro del modelo Category en el panel de administración
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']       # Define las columnas que se mostrarán en la lista de categorías
    prepopulated_fields = {'slug': ('name',)}       # Permite que el campo 'slug' se genere automáticamente a partir del 'name'

@admin.register(Product)   # Registro del modelo Product en el panel de administración
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',       # Define las columnas que se mostrarán en la lista de productos
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']       # Agrega filtros para facilitar la búsqueda de productos según su estado y fecha
    list_editable = ['price', 'available']    # Permite la edición en línea de los campos 'price' y 'available' desde la lista
    prepopulated_fields = {'slug': ('name',)}   # Permite que el campo 'slug' se genere automáticamente a partir del 'name'
