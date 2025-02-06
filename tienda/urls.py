from django.contrib import admin
from django.urls import include, path
from tienda.views  import *
from tienda import views
urlpatterns = [
    path('productos/crear', CrearProductos.as_view(), name='crear'),
    path("listadoproductos/", ListadoProductos.as_view(), name="listadoProductos"),
    path("detalleproductos/<int:pk>", DetalleProductos.as_view(), name="detalleProductos"),
    path('productos/<int:pk>/edit', EditarProductos.as_view(), name='producto_editar'),
    path('productos/<int:pk>/del', BorrarProductos.as_view(), name='producto_borrar'),
    path('compras', ListadoCompras.as_view(), name='compras'),
    path('confirmaCompra/<int:pk>', ConfirmaCompra.as_view(), name='confirmaCompra'),
    path('informes', views.informes, name='informes'),
    path('perfil', Perfil.as_view(), name='perfil'),
    
]
