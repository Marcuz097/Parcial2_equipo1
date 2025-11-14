from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .models import Proveedor
from .models import Producto

#importar reverse_lazy de urls para redireccionar la respuesta de un formulario
from django.urls import reverse_lazy

from .forms import CategoriaForm
from .forms import ProveedorForm
from .forms import ProductoForm

# Create your views here.

# crear vistas genericas para categoria
class CategoriaListView(ListView):

    # indicar cual es el modelo base
    model = Categoria
    fields = ["nombre", "descripcion"]
    template_name = "categorias/categoria-list.html"
    context_object_name = "categorias"


# crear vistas genericas para categoria
class CategoriaCreateView(CreateView):
    # indicar cual es el modelo base
    model = Categoria
    form_class = CategoriaForm
    template_name = "categorias/categoria-form.html"
    success_url = reverse_lazy("productos:categoria-list")
#Proovedores 

class ProveedorListView(ListView):

    # indicar cual es el modelo base
    model = Proveedor
    fields = ["nombre", "telefono", "contacto"]
    template_name = "proveedores/proveedor-list.html"
    context_object_name = "proveedores"

# crear vistas genericas para categoria
class ProveedorCreateView(CreateView):
    # indicar cual es el modelo base
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedores/proveedor-form.html"
    success_url = reverse_lazy("productos:proveedor-list")

# 1. ListView: Mostrar todos los productos
class ProductoListView(ListView):
    model = Producto
    # La ruta a tu plantilla de lista
    template_name = "productos/producto-list.html" 
    # Nombre de la variable en la plantilla
    context_object_name = "productos" 

# 2. CreateView: Registrar nuevos productos
class ProductoCreateView(CreateView):
    model = Producto
    # Campos que aparecerán en el formulario
    form_class = ProductoForm 
    # La ruta a tu plantilla de formulario
    template_name = "productos/producto-form.html" 
    # Redirige a la lista después de guardar
    success_url = reverse_lazy("productos:producto-list") 

# 3. (BONUS) UpdateView: Editar un producto existente
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio_compra', 'precio_venta', 'descripcion', 'categoria', 'proveedor']
    template_name = "productos/producto-form.html"
    success_url = reverse_lazy("productos:producto-list")

# 4. (BONUS) DeleteView: Eliminar un producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto-delete.html" # Plantilla para confirmar eliminación
    success_url = reverse_lazy("productos:producto-list") 
