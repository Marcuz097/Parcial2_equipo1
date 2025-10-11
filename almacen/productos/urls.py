# archivo de enrutamiento de la aplicación productos
from django.urls import path
# importando las vistas
from .views import (
    CategoriaListView,
    CategoriaCreateView,
    ProveedorListView,
    ProveedorCreateView,
    #Productos
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

# agregar un identificador de enrutamiento
app_name = "productos"

# enrutamiento
urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name="categoria-list"),
    path('categorias/nueva', CategoriaCreateView.as_view(), name="categoria-create"),
    #proveedores
    path('proveedores/', ProveedorListView.as_view(), name="proveedor-list"),
    path('proveedores/nueva', ProveedorCreateView.as_view(), name="proveedor-create"),
    #Productos
     # Rutas de Producto
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    
    # Rutas BONUS
    path('productos/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto-delete'),
]
