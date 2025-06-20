# 🛍️ Tienda Virtual - Proyecto Django

**TiendaVirtual** es una aplicación web de comercio electrónico desarrollada con **Django 5.1.3**, que permite gestionar productos, usuarios, compras y promociones, incluyendo informes detallados y control de permisos por rol.

> 📚 Documentación y aportes en [@dsevillanonavarro en DeepWiki](https://deepwiki.com/u/dsevillanonavarro)

---

## 🎯 Objetivo del Proyecto

Este proyecto busca reforzar habilidades clave de desarrollo web backend con Django:

- Modelado de datos relacional (ORM)
- Formularios dinámicos y validaciones
- Sistema de autenticación personalizado
- Permisos según tipo de usuario
- Flujo completo de compra
- Generación de informes y visualización de datos

---

## 🧱 Estructura del Proyecto

```bash
dsevillanonavarro-tiendavirtual/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── tienda/                     # App principal
│   ├── admin.py                # Registro de modelos en el admin
│   ├── models.py               # Usuario, Producto, Marca, Compra
│   ├── views.py                # CRUD, compras, informes
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   └── tienda/             # Templates HTML (Bootstrap 5)
│   └── migrations/
├── tiendavirtual/              # Configuración global de Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
🚀 Funcionalidades
🛒 Sistema de Compras
Vista de productos con filtros por nombre, marca y precio.

Vista detallada de producto con imagen.

Formulario de compra con control de stock y saldo.

IVA calculado automáticamente.

🧑‍💼 Gestión de Usuarios
Login personalizado (solo clientes pueden loguearse).

Redirección tras login al último intento.

Vista de perfil con historial de compras y saldo.

🔐 Permisos y Seguridad
Acceso público a listado y detalle de productos.

Checkout solo para clientes autenticados.

CRUD y sección de informes solo para staff o superuser.

⚙️ CRUD de Productos y Promociones
Alta, edición y eliminación de productos y promociones.

Asociación de productos con marcas.

Aplicación de códigos de promoción en el checkout.

📊 Informes
Top 10 productos más vendidos.

Top 10 clientes con mayor gasto.

Detalle de compras por usuario.

Estadísticas de uso de promociones.

📦 Requisitos del Proyecto
Python 3.10+

Django 5.1.3

Pillow

mysql-connector-python (opcional)

Instalación:

bash
Copiar
Editar
pip install -r requirements.txt
⚙️ Configuración Inicial
bash
Copiar
Editar
# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver
Configuración de archivos multimedia en settings.py:

python
Copiar
Editar
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
🖼️ Interfaz de Usuario
Uso de Bootstrap 5 en todos los templates.

Formularios estilizados automáticamente.

Alertas con el sistema de mensajes de Django.

Navegación clara y lógica para usuarios y administradores.

🧪 Recomendaciones para Probar
Loguearse como superusuario para acceder al CRUD y sección de informes.

Crear un usuario cliente con saldo y hacer compras.

Probar la aplicación de promociones al comprar.

Usar los filtros en la vista de productos.

📍 Futuras Mejoras (To-Do)
Registro de clientes desde el frontend.

Integración de pasarelas de pago simuladas.

Exportación de facturas en PDF.

Envío de emails automáticos tras compras.

Filtros más avanzados por fecha, precio, stock, etc.

👨‍💻 Autor
Este proyecto fue desarrollado por @dsevillanonavarro en DeepWiki.
Puedes seguir allí la documentación detallada y otros aportes del autor.

📃 Licencia
Este proyecto está licenciado bajo la MIT License. Puedes usarlo, modificarlo y distribuirlo libremente.

yaml
Copiar
Editar

---

¿Te gustaría que también te genere un `README.md` descargable como archivo o lo subo automáticamente al proyecto si me das acces