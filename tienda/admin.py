from django.contrib import admin
from .models import Producto, Compra, Usuario, Marca
# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Compra)
admin.site.register(Usuario)