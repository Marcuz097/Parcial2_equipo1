from django.db import models

# Create your models here.

#tabla categoria o modelos
class Categoria(models.Model): #aplicar herencia de models.Model

    #crear las propiedades de la clase categoria 
    nombre = models.CharField(max_length=50, unique=True) #nombre varchar(50) not null
    descripcion = models.TextField(max_length=255, null=True, blank=True) #descripcion text not null

     #Ajuste a la tabla y modelos => 's o => oes
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre'] #ordenar por nombre

        # 💡 IMPLEMENTAR ESTE MÉTODO
    def __str__(self):
        # Retorna el campo que quieres ver (ej: el nombre)
        return self.nombre
    

#tabla proveedor o modelos 
class Proveedor(models.Model): #aplicar herencia de models.Model

    #crear las propiedades de la clase proveedor 
    nombre = models.CharField(max_length=50) #nombre varchar(50) not null
    direccion = models.TextField(max_length=255, null=True, blank=True) #direccion text not null
    telefono = models.CharField(max_length=20, null=True, blank=True) #telefono varchar(15) not null
    email = models.EmailField(null=True, blank=True) #email varchar(254) not null
    contacto = models.CharField(max_length=100, null=True, blank=True) #contacto varchar(50) not null


    #Ajuste a la tabla y modelos => 's o => oes
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre'] #ordenar por nombre

         # 💡 IMPLEMENTAR ESTE MÉTODO
    def __str__(self):
        # Retorna el campo que quieres ver (ej: el nombre)
        return self.nombre



#Crear un clave que represente mis productos en la base de datos (BD)
class Producto(models.Model): #aplicar herencia de models.Model

    #crear las propiedades de la clase producto 
    nombre = models.CharField(max_length=50) #nombre varchar(50) not null
    precio_compra = models.DecimalField(max_digits=12, decimal_places=2) #precio decimal(12,2) not null
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2) #precio decimal(12,2) not null
    descripcion = models.TextField(null=True, max_length=150) #descripcion text not null
    #Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    #Proveedor
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) 

#Ajuste a la tabla y modelos => 's o => oes
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre'] #ordenar por nombre



    # Crear metodo
    def __str__(self):
        return f"{self.nombre} - {self.stock}unidades"