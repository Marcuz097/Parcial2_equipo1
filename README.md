# Parcial2_equipo1

Equipo #1

Integrantes:      
Yeyson Elber Aguilar Echeverria

David Alexander Borja Abrego

Heriberto Josue Echeverria Cardona 

Marco Antonio Orellana Guardado 

Ludy Amarillis Pineda Lemus 

Jennifer Susana Ruiz Mendez 

# Rutas implementadas

 # Rutas de Producto
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    
    # Rutas BONUS
    path('productos/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto-delete'),

# Breve descripción del funcionamiento. 

El módulo de Productos permite gestionar toda la información relacionada con los artículos o productos del sistema.
Su funcionamiento se basa en operaciones CRUD (Crear, Leer, Actualizar y Eliminar) utilizando las vistas y rutas definidas en Django.

Funcionamiento general:

🔹 Listado de productos:
Muestra todos los productos registrados en la base de datos en una tabla o lista.
(Ruta típica: /productos/)

🔹 Agregar producto:
Desde un formulario, el usuario puede registrar un nuevo producto con sus datos (nombre, precio, cantidad, descripción, etc.).
(Ruta típica: /productos/agregar/)

🔹 Editar producto:
Permite modificar la información de un producto existente seleccionándolo desde la lista.
(Ruta típica: /productos/editar/<id>/)

🔹 Eliminar producto:
Elimina el registro de un producto del sistema.
(Ruta típica: /productos/eliminar/<id>/)

Todo esto se realiza mediante las vistas de Django, que conectan los modelos de la base de datos con las plantillas HTML, permitiendo al usuario interactuar con los datos de forma sencilla.
    


