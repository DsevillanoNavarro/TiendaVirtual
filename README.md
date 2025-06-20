# 🛍️ Tienda Virtual - Proyecto Django

Bienvenido a **TiendaVirtual**, una aplicación web de comercio electrónico desarrollada con **Django 5.1.3**. Este proyecto ofrece funcionalidades completas de gestión de productos, autenticación de usuarios, proceso de compra, informes de negocio y control de permisos.

> ✍️ Autor: [@dsevillanonavarro en DeepWiki](https://deepwiki.com/u/dsevillanonavarro)

---

## 🎯 Objetivo del Proyecto

El objetivo principal de este proyecto es afianzar los conocimientos de Django en aspectos clave como:

- Modelado de datos
- Formularios
- Autenticación personalizada
- Permisos de usuario
- Generación de informes
- Flujo completo de compra

Está pensado como una práctica completa para proyectos de desarrollo web en Python/Django.

---

## 🧱 Estructura del Proyecto

dsevillanonavarro-tiendavirtual/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── tienda/ # App principal
│ ├── admin.py # Registro de modelos
│ ├── models.py # Usuario, Producto, Compra, Marca
│ ├── views.py # CRUD, compra, informes
│ ├── forms.py
│ ├── urls.py
│ ├── templates/
│ │ └── tienda/ # Templates: productos, compras, perfil, etc.
│ └── migrations/
├── tiendavirtual/ # Configuración del proyecto Django
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py

---

## 🚀 Funcionalidades

### 🛒 Compras
- Listado de productos con filtros por nombre, precio y marca.
- Vista detallada del producto.
- Checkout con confirmación y control de saldo y stock.
- Compra registrada con IVA e importe total.

### 🧑‍💼 Gestión de Usuarios
- Login personalizado sólo para clientes registrados.
- Visualización del estado de autenticación en base.html.
- Panel de perfil con historial de compras.

### 🔐 Control de Permisos
- Secciones protegidas por tipo de usuario:
  - CRUD e informes: solo staff/superuser.
  - Checkout: solo clientes logueados.
  - Vista de productos: acceso público.

### ⚙️ CRUD de Productos y Promociones
- Crear, editar, eliminar y listar productos.
- Asociar productos con marcas.
- Promociones (v2.0): aplicar descuentos desde el checkout con códigos.

### 📊 Informes
- Top 10 productos más vendidos.
- Top 10 clientes por importe gastado.
- Listado de compras por usuario.
- Informe detallado de promociones utilizadas.

---

## 📦 Requisitos

- Python 3.10+
- Django 5.1.3
- Pillow
- mysql-connector-python (opcional)

Instalación de dependencias:

```bash
pip install -r requirements.txt
⚙️ Configuración Inicial
bash
Copiar
Editar
# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor local
python manage.py runserver
Archivos multimedia se sirven desde:

python
Copiar
Editar
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
🖼️ Interfaz de Usuario
Templates con Bootstrap 5

Formularios estilizados automáticamente

Alertas y validaciones con mensajes Django

Navegación intuitiva

🧪 Funcionalidad de Prueba
Usa el superusuario para probar el CRUD y los informes

Crea un usuario cliente con saldo y realiza compras

Aplica promociones desde el checkout

📍 Próximas Funcionalidades (ideas)
Registro de usuarios en frontend

Soporte para métodos de pago simulados

Generación de facturas en PDF

Notificaciones por email

Filtros avanzados en informes

👨‍💻 Autor
Este proyecto fue desarrollado por @dsevillanonavarro en DeepWiki.
Puedes seguir mis aportes y otros proyectos allí.

📃 Licencia
Este proyecto está licenciado bajo MIT. Eres libre de usar, modificar y compartir.

yaml
Copiar
Editar

---

¿Quieres que además te genere un archivo `README.md` descargable o incluir badges (build, licencia, versión de Django, 