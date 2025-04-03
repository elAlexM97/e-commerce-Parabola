from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None  # Se agrega una variable para almacenar la categoría seleccionada
    categories = Category.objects.all()  # Se obtienen todas las categorías de la base de datos
    products = Product.objects.filter(available=True)  # Se filtran solo los productos disponibles
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)  # Se obtiene la categoría específica por slug
        products = products.filter(category=category)  # Se filtran los productos según la categoría seleccionada
    return render(request, 
                  'shop/product/list.html', 
                  {'category': category,  # Se pasa la categoría seleccionada al template
                   'categories': categories,  # Se pasan todas las categorías al template
                   'products': products})  # Se pasan los productos filtrados al template

def product_detail(request, id, slug):
    product = get_object_or_404(Product, 
                                id=id, 
                                slug=slug, 
                                available=True)  # Se obtiene el producto por ID y slug, si está disponible
    cart_product_form = CartAddProductForm()  # Se crea una instancia del formulario para agregar al carrito
    return render(request, 
                  'shop/product/detail.html', 
                  {'product': product,  # Se pasa el producto al template
                   'cart_product_form': cart_product_form})  # Se pasa el formulario del carrito al template

def mapa(request):
    # Coordenadas de la bibliote de la UTCH:
    lat_default = 28.642433   # latitud
    lon_default = -106.145414 # longitud

    lat = lat_default  # Se inicializa la latitud
    lon = lon_default  # Se inicializa la longitud

    if request.method == 'POST':  # Se verifica si la solicitud es tipo POST
        try:
            lat = float(request.POST.get('lat', lat_default))  # Se obtiene la latitud
            lon = float(request.POST.get('lon', lon_default))  # Se obtiene la longitud
            
            # Se valida que las coordenadas estén dentro del rango permitido
            if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
                raise ValueError("Coordenadas fuera de rango")  # Se genera un error si los valores están fuera de rango
                
        except (ValueError, TypeError):  # Si hay un error en la conversión, se restablecen los valores por defecto
            lat = lat_default
            lon = lon_default

    return render(request, 'map.html', {
        'lat': lat,  # latitud al template
        'lon': lon   # longitud al template
    })

    context = {
        'lat': lat,
        'lon': lon
    }
    return render(request, 'map.html', context)  # se renderiza la plantilla con las coordenadas
