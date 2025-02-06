from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    vip = models.BooleanField(default=False, blank=True)
    saldo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00)
    
    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
class Marca(models.Model):
    nombre = models.CharField(max_length=50,blank=False,unique=True)
    
    def __str__(self):
        return f'{self.nombre}'
        
class Producto(models.Model):
    nombre = models.CharField(max_length=50,blank=False)
    foto = models.ImageField(upload_to='producto/', null=True, blank=True)
    marca = models.ForeignKey("Marca",on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    unidades = models.PositiveIntegerField()
    precio = models.FloatField()
    vip = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = ['nombre', 'marca']
        
    def __str__(self):
        return  f'{self.nombre}'
class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    unidades = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    importe = models.IntegerField()
    iva = models.DecimalField(default=0.21, decimal_places=2, max_digits=5)
    def __str__(self):
        return f'{self.usuario}'
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = 'Compras'
        unique_together = ['usuario', 'producto','fecha']