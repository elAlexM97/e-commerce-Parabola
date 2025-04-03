from django import forms
from .models import Order

# se define un formulario para capturar la información de los usuarios al realizar una orden de compra
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order  # Se vincula con el modelo de órdenes
        fields = ['first_name', 'last_name', 'email', 'address',  # Campos que debe llenar el usuario
                  'postal_code', 'city']