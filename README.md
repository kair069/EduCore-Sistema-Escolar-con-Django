# 🏫 EduCore - Sistema Escolar con Django

![EduCore Screenshot](https://github.com/kair069/EduCore-Sistema-Escolar-con-Django/blob/main/codeedu.JPG)

**EduCore** es una plataforma web desarrollada en Django que permite la gestión integral de instituciones educativas. El sistema está diseñado bajo el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** y cuenta con funcionalidades completas para la administración académica y operativa de un colegio, con énfasis en la **seguridad** y el control de acceso basado en roles.

---

## 🔐 Seguridad y control de acceso

- Sistema de autenticación con inicio de sesión seguro
- Control de acceso por roles: administrador, docente, estudiante, etc.
- Validación de formularios y protección contra entradas maliciosas
- Gestión de permisos por grupo de usuarios

---

## ✨ Funcionalidades principales

- ✔️ Gestión de usuarios (estudiantes, docentes, personal administrativo)
- ✔️ Registro y control de asistencias por curso y fecha
- ✔️ Evaluaciones, calificaciones y trabajos escolares
- ✔️ Asignación de materias y módulos para docentes
- ✔️ Panel administrativo completo con filtros y gestión dinámica
- ✔️ Arquitectura MVC clara para facilitar el mantenimiento y la escalabilidad

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Django
- HTML5, CSS3, Bootstrap
- SQLite3 (o PostgreSQL/MySQL)
- Git & GitHub

---

## 🚀 Cómo ejecutar el proyecto en local

```bash
# Clonar el repositorio
git clone https://github.com/kair069/EduCore-Sistema-Escolar-con-Django.git
cd EduCore-Sistema-Escolar-con-Django

# Crear entorno virtual
python -m venv env
# Activar el entorno (Windows)
env\Scripts\activate
# Activar en Linux/Mac
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Iniciar el servidor
python manage.py runserver

📂 Estructura del proyecto (basado en MVC)

EduCore/
├── core/                  # Modelos, Vistas y Controladores por módulo
├── templates/             # Vistas (HTML)
├── static/                # Archivos estáticos (CSS, JS)
├── media/                 # Archivos subidos
├── db.sqlite3             # Base de datos local
├── manage.py              # Script principal de Django
└── requirements.txt       # Dependencias del proyecto

📌 Autor
Desarrollado por @kair069

Proyecto educativo de sistema escolar con Django, enfoque seguro y modular
