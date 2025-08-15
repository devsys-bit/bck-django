#!/bin/bash
set -e  # Detener si algún comando falla

# 1. Drop & Create DB en Supabase
PGPASSWORD="GMzACopxKh4lQ2vL" psql \
  -h db.przjtdpwdtbbivfgdojd.supabase.co \
  -U postgres \
  -d template1 \
  -c "DROP DATABASE IF EXISTS postgres;" \
  -c "CREATE DATABASE postgres;"

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Migraciones generales
python manage.py migrate

# 4. Migraciones específicas de la app `task`
python manage.py makemigrations task
python manage.py sqlmigrate task 0001
python manage.py migrate task

# 5. Recolectar archivos estáticos
python manage.py collectstatic --noinput
