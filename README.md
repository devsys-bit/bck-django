# Backend Django - Task API

Este backend implementa la API REST de **Task** usando **Django** y **Django REST Framework**.  
Permite gestionar tareas con operaciones de alta, consulta, edición parcial, borrado lógico y restauración.

---

## 📌 Endpoints disponibles

| Método | URL | Descripción |
|--------|-----------------------------|------------------------------------|
| GET    | `/task/`                    | Listar todas las tareas (findAll)  |
| GET    | `/task/<int:pk>/`           | Obtener una tarea por ID (findOne) |
| POST   | `/task/`                    | Crear una nueva tarea (create)     |
| PATCH  | `/task/update/<int:pk>/`    | Actualizar parcialmente una tarea (update parcial) |
| DELETE | `/task/remove/<int:pk>/`    | Eliminar lógicamente una tarea (remove) |
| PATCH  | `/task/restore/<int:pk>/`   | Restaurar una tarea eliminada (restore) |

---

## ⚙️ Instalación

### 1. Clonar solo este backend

Si solo quieres el backend Django, clona directamente este repositorio:

```bash
git clone https://github.com/devsys-bit/bck-django.git
cd bck-django
```

---

### 2. Crear entorno virtual, activarlo y actualizar pip

```bash
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate         # Windows

python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz de `bck-django` con el siguiente contenido (ajusta los valores según tu configuración):

```
USER_DB=tu_usuario
PASSWORD_DB=tu_contraseña
HOST_DB=tu_host
PORT_DB=tu_puerto
NAME_DB=tu_base_datos
```

> ⚠️ **Este backend está configurado para usar PostgreSQL como base de datos.**  
> Si quieres usar otro motor, ajusta la configuración en `settings.py`.

---

### 4. Migrar base de datos

Ejecuta los siguientes comandos para aplicar las migraciones:

```bash
# Aplica migraciones iniciales de Django (auth, admin, etc.)
python manage.py migrate

# Crea migraciones para la app "task"
python manage.py makemigrations task
```

> Cuando ejecutes `makemigrations task`, Django mostrará un mensaje similar a:
>
> ```
> Migrations for 'task':
>   task/migrations/0001_initial.py
> ```
> El número **0001** (o similar) es el identificador de la migración.

```bash
# (Opcional) Ver el SQL de la migración antes de aplicarla:
python manage.py sqlmigrate task 0001

# Aplica las migraciones de la app "task"
python manage.py migrate task
```

💡 **Nota:** Si modificas los modelos en el futuro, repite `makemigrations task` y `migrate`.

---

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

La API estará disponible en:  
👉 `http://127.0.0.1:8000`

---

## 📌 Notas

- El backend usa **PostgreSQL** como base de datos por defecto.
- El borrado es **lógico**: las tareas no se eliminan físicamente, solo se marca la fecha en `deleted_at`.
- El endpoint `/task/restore/<int:pk>/` permite reactivar tareas eliminadas.

---

## ✍️ Autor

**DERLYS DANIEL ALVARADO MENDOZA**  
Desarrollador Web Full Stack