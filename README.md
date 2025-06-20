# 🛍️ Tienda Virtual - Proyecto Django

**TiendaVirtual** es una aplicación web de comercio electrónico desarrollada con **Django 5.1.3**, que permite gestionar productos, usuarios, compras y promociones, incluyendo informes detallados y control de permisos por rol.

> 📚 Documentación y aportes en [DeepWiki](https://deepwiki.com/DsevillanoNavarro/TiendaVirtual)

---

## 🎯 Objetivo del Proyecto

Este proyecto busca reforzar habilidades clave de desarrollo web backend con Django:

- Modelado de datos relacional (ORM).
- Formularios dinámicos y validaciones.
- Sistema de autenticación personalizado.
- Control de permisos según tipo de usuario.
- Flujo completo de compra con control de stock y saldo.
- Generación de informes y visualización de datos.
- Gestión de promociones y aplicación de códigos de descuento.

Está diseñado como práctica completa para entender un flujo real de aplicación de comercio electrónico en Django.

---

## 🧱 Estructura del Proyecto

```
dsevillanonavarro-tiendavirtual/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── tienda/                     # App principal
│   ├── admin.py                # Registro de modelos en el admin
│   ├── models.py               # Modelos: Usuario, Producto, Marca, Compra
│   ├── views.py                # Lógica de CRUD, compras e informes
│   ├── forms.py                # Formularios (p. ej., CompraForm)
│   ├── urls.py                 # Rutas de la app 'tienda'
│   ├── templates/
│   │   └── tienda/             # Templates HTML con Bootstrap 5
│   │       ├── base.html
│   │       ├── listadoProductos.html
│   │       ├── detalleProductos.html
│   │       ├── crearProducto.html
│   │       ├── editarProducto.html
│   │       ├── producto_confirm_delete.html
│   │       ├── listadoCompras.html
│   │       ├── confirmCompra.html
│   │       ├── perfil.html
│   │       ├── informes.html
│   │       └── registration/login.html
│   └── migrations/             # Archivos de migraciones
├── tiendavirtual/              # Proyecto Django
│   ├── settings.py             # Configuración global
│   ├── urls.py                 # Rutas del proyecto
│   ├── wsgi.py
│   └── asgi.py
└── media/                      # Directorio de carga de imágenes (configurable)
```

- **manage.py**: utilidad de línea de comandos de Django.
- **requirements.txt**: dependencias del proyecto.
- **db.sqlite3**: base de datos SQLite para desarrollo (no versionar en producción).

---

## 🚀 Funcionalidades Principales

### 🛒 Sistema de Compras
- Listado de productos con filtros por nombre, marca y precio.
- Vista detallada de producto con imagen y datos relevantes (modelo, precio, unidades, estado VIP).
- Proceso de compra:
  - Formulario de unidades a comprar.
  - Confirmación previa mostrando total calculado (precio × unidades).
  - Control de stock: verificación de disponibilidad.
  - Control de saldo de usuario: verificación de saldo suficiente.
  - Registro de la compra con importe, IVA y fecha.
  - Actualización automática de stock y saldo.

### 🧑‍💼 Gestión de Usuarios
- Modelo de usuario personalizado (`Usuario`) extendiendo `AbstractUser`, con campos adicionales (`vip`, `saldo`).
- Login personalizado: solo usuarios tipo cliente pueden iniciar sesión.
- Redirección tras login al último destino solicitado.
- Vista de perfil:
  - Visualización de saldo.
  - Historial de compras paginado.
  - Enlaces a detalle de cada compra/producto.

### 🔐 Permisos y Seguridad
- Acceso público a:
  - Listado de productos.
  - Detalle de producto.
- Acceso restringido a clientes autenticados:
  - Checkout/confirmación de compra.
  - Perfil e historial de compras.
- Acceso restringido a staff/superuser:
  - CRUD de productos y de promociones.
  - Sección de informes.

### ⚙️ CRUD de Productos y Promociones
- **Productos**:
  - Crear producto con foto, marca, modelo, precio, unidades y flag VIP.
  - Editar y eliminar producto.
  - Listado en admin y en interfaz personalizada.
  - Validaciones (por ejemplo, combinación única de nombre + marca).
- **Promociones (versión 2.0)**:
  - Modelo de promoción con código, descripción, fecha de validez, porcentaje o importe de descuento, condiciones (p. ej., mínimo de compra).
  - CRUD de promociones en área de administración.
  - En checkout, posibilidad de introducir código de promoción:
    - Validación de aplicabilidad (vigencia, condiciones, uso previo, etc.).
    - Cálculo de descuento y mostrar importe final antes de confirmar.
- (Nota: si aún no implementas promociones, omitir o comentar la sección en README hasta añadir el modelo y lógica correspondiente).

### 📊 Informes
- Top 10 productos más vendidos (por número de unidades).
- Top 10 clientes con mayor gasto acumulado.
- Listado y detalle de compras por usuario.
- Estadísticas de uso de promociones:
  - Número de compras con cada promoción.
  - Descuento medio aplicado.
  - Total de importe promocionado.
- Estas vistas están protegidas para `staff` o `superuser`.

---

## 📦 Requisitos

- Python 3.10 o superior.
- Django 5.1.3.
- Pillow (para manejo de imágenes).
- mysql-connector-python (opcional, si se desea usar MySQL en lugar de SQLite).
- Otras dependencias que figuren en `requirements.txt`.

Contenido de ejemplo en `requirements.txt`:
```text
Django==5.1.3
Pillow
mysql-connector-python==9.2.0
```

---

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu-usuario/tiendavirtual.git
   cd tiendavirtual
   ```

2. **Crear y activar entorno virtual** (recomendado)  
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/macOS
   # venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**  
   - Por defecto usa SQLite (`db.sqlite3`).  
   - Si quieres MySQL, editar `tiendavirtual/settings.py` en `DATABASES`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'nombre_bd',
             'USER': 'usuario_bd',
             'PASSWORD': 'tu_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Aplicar migraciones**  
   ```bash
   python manage.py migrate
   ```

6. **Crear superusuario**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Configurar archivos multimedia** (imágenes de producto)  
   En `tiendavirtual/settings.py`:
   ```python
   MEDIA_ROOT = BASE_DIR / 'media'
   MEDIA_URL = '/media/'
   ```
   En `tiendavirtual/urls.py`:
   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       # ... tus rutas ...
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

8. **Ejecutar servidor de desarrollo**  
   ```bash
   python manage.py runserver
   ```
   Acceder en navegador a `http://127.0.0.1:8000/`.

---

## 🔧 Configuración Adicional de Autenticación

- En `settings.py`, se define:
  ```python
  AUTH_USER_MODEL = 'tienda.Usuario'
  LOGIN_REDIRECT_URL = 'compras'
  LOGOUT_REDIRECT_URL = 'compras'
  ```
- Templates de login personalizados en `tienda/templates/registration/login.html`.
- Verificar en vistas y URLs que solo clientes pueden autenticarse (si es necesario, añadir validaciones en la vista de login).

---

## 🧪 Pruebas y Validación

1. **Probar CRUD de productos**  
   - Acceder como superusuario.  
   - Crear marcas y productos con foto, precio y stock.  
   - Editar y eliminar para verificar validaciones y mensajes.

2. **Probar usuario cliente**  
   - Crear usuario cliente en admin o frontend.  
   - Ajustar saldo para pruebas.

3. **Probar flujo de compra**  
   - Iniciar sesión como cliente.  
   - Filtrar y seleccionar producto, especificar unidades.  
   - Confirmar compra: verificar actualización de stock y saldo.  
   - Intentar comprar con saldo insuficiente o stock insuficiente: mensajes de error.

4. **Probar promociones**  
   - Crear promociones en admin con código, fechas y condiciones.  
   - Ingresar código en checkout: verificar descuento o rechazos por vigencia/condiciones.

5. **Probar informes**  
   - Acceder a informes como superusuario.  
   - Verificar Top 10 productos y clientes, detalle de compras y estadísticas de promociones.

6. **Verificar manejo de medios**  
   - Subir imágenes de producto y acceder desde la vista de detalle.

7. **Pruebas de permisos**  
   - Intentar acceder a URLs restringidas sin autenticación o con permisos insuficientes: redirección o error.

---

## 📍 Futuras Mejoras

- Registro de clientes desde frontend con confirmación por email.
- Integración de pasarelas de pago (Stripe, PayPal) en entornos de prueba.
- Generación de facturas en PDF (ReportLab, WeasyPrint).
- Envío de emails automáticos tras confirmación de compra o restablecimiento de contraseña.
- Dashboard de administración con gráficos avanzados.
- Filtros adicionales en vistas de productos (rango de fechas, categorías, etiquetas).
- Internacionalización y localización (i18n, l10n).
- Tests automatizados (unitarios e integración) para modelos y vistas.
- Caché de consultas frecuentes para mejorar rendimiento.
- Paginación y optimización de carga de imágenes en listados largos.
- Documentación extendida en DeepWiki: diagramas de flujo, modelo de datos y ejemplos de uso.

---

## 👨‍💻 Autor

Desarrollado por **@dsevillanonavarro**.  
Para documentación detallada y guía completa del proyecto, visita: [Documentación de TiendaVirtual en DeepWiki](https://deepwiki.com/DsevillanoNavarro/TiendaVirtual).
## 📃 Licencia

Este proyecto está licenciado bajo la **MIT License**.  
Puedes usarlo, modificarlo y distribuirlo libremente.
