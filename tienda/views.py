from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from .models import Usuario, Producto, Compra, Marca
from .forms import CompraForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from django.contrib.admin.views.decorators import staff_member_required
class ListadoProductos(ListView):
    model = Producto
    template_name = 'tienda/listadoProductos.html'
    context_object_name = 'productos'


class ListadoCompras(ListView):
    model = Producto
    template_name = 'tienda/listadoCompras.html'
    context_object_name = 'productos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        marcas = Marca.objects.filter(producto__isnull=False).distinct()
        contexto['marcas'] = marcas
        form = CompraForm()
        contexto['compraForm'] = form
        return contexto
    
    
    def get_queryset(self):
            query = super().get_queryset()
            filtro_nombre = self.request.GET.get('filtro_nombre')
            filtro_marca = self.request.GET.get('filtro_marca')
            filtro_precio_max = self.request.GET.get('filtro_precio_max')

            if filtro_nombre:
                query = query.filter(nombre__icontains=filtro_nombre)

            if filtro_marca:
                query = query.filter(marca__nombre=filtro_marca)

            if filtro_precio_max:
                query = query.filter(precio__lte=filtro_precio_max)

            return query
    

class DetalleProductos(DetailView):
    model = Producto
    template_name = 'tienda/detalleProductos.html'


class EditarProductos (UpdateView):
    model = Producto
    template_name = 'tienda/editarProducto.html'
    fields = '__all__'
    success_url = reverse_lazy("listadoProductos")


class BorrarProductos (DeleteView):
    model = Producto
    success_url = reverse_lazy("listadoProductos")


class CrearProductos(CreateView):
    model = Producto
    template_name = 'tienda/crearProducto.html'
    fields = '__all__'
    success_url = reverse_lazy("listadoProductos")
    
    
class ConfirmaCompra(View):
    
    
    def get (self,request,pk):
        prod = get_object_or_404(Producto,pk=pk)
        unid = request.GET.get('unidades')
        total = prod.precio * int(unid)
        return render(request, 'tienda/confirmCompra.html', {'producto':prod, 'unidades':unid, 'total':total})
    def post (self,request,pk):
        prod = get_object_or_404(Producto,pk=pk)
        unid = request.POST.get('unidades')
        usuario = request.user
        total = prod.precio * int(unid)
        
        if prod.unidades >= int(unid):
            if usuario.saldo >= total:
                usuario.saldo = usuario.saldo-int(total)
                prod.unidades = prod.unidades-int(unid)
                compra = Compra(usuario=usuario, unidades=int(unid), producto=prod, importe=int(total))
                compra.save()
                usuario.save()
                prod.save()
                messages.success(request, 'Compra hecha.')
                return redirect('compras')
            else:
                messages.error(request, 'Saldo insuficiente')
                return redirect('compras')
        else:
            messages.error(request, 'Unidades insuficientes')
            return redirect('compras')
        
        
class ComprarProducto(ListView):
    model = Producto
    
@staff_member_required
def informes(request):
    topclients = Usuario.objects.annotate(importe_compras = Sum('compra__importe'), total_compras = Count('compra')).order_by('-importe_compras')[:10]
    topproductos = Producto.objects.annotate(total_vendidos = Sum('compra__unidades')).order_by('-total_vendidos')[:10]
    return render(request,'tienda/informes.html',{'topclients':topclients,'topproductos':topproductos})

class Perfil (ListView):
    model = Compra
    template_name = 'tienda/perfil.html'
    context_object_name = 'compraUser'
    paginate_by = 3
def get_queryset(self):
            query = super().get_queryset()
            
            query = query.filter(usuario = self.request.user)
            return query