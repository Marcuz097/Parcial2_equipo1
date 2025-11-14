from django import forms
from .models import Categoria
from .models import Proveedor
from .models import Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoria'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Descripccion Categoria','rows': 3}),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Telefono del proveedor'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contacto del proveedor'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_compra', 'precio_venta', 'descripcion', 'categoria', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio de compra'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio de venta'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Descripción del producto','rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }
        