from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

from django.db import models

class Nivel(models.Model):
    nombre = models.CharField(max_length=50)  # Primaria o Secundaria
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(blank=True, null=True, default="Descripción no disponible")  # Descripción por defecto
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo')
    años_duracion = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='niveles/', blank=True, null=True)  # Imagen opcional
    #Ultima Agregacion
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)  # Agregamos el creador

    def __str__(self):
        return self.nombre


# class Grado(models.Model):
#     nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=50)  # Ejemplo: "1° de Secundaria"

#     def __str__(self):
#         return f"{self.nombre} - {self.nivel}"
from django.db import models

from django.db import models

class Grado(models.Model):
    GRADOS_CHOICES = [
        ('1°', '1°'),
        ('2°', '2°'),
        ('3°', '3°'),
        ('4°', '4°'),
        ('5°', '5°'),
        ('6°', '6°'),
    ]

    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name="grados")
    nombre = models.CharField(max_length=2, choices=GRADOS_CHOICES, help_text="Selecciona el grado")
    descripcion = models.TextField(blank=True, null=True, default="Descripción no disponible", help_text="Descripción opcional del grado")
    imagen = models.URLField(blank=True, null=True, help_text="Enlace a una imagen representativa del grado")

    def __str__(self):
        return f"{self.nombre} ({self.nivel.nombre})"



class Seccion(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=5)  # Ejemplo: "A", "B"

    def __str__(self):
        return f"{self.grado} - Sección {self.nombre}"

class Periodo(models.Model):
    nombre = models.CharField(max_length=20)  # Ejemplo: "1er Bimestre", "2do Trimestre"
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

# class Curso(models.Model):
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField(blank=True)

#     def __str__(self):
#         return self.nombre
class Curso(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="cursos")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.grado.nombre} ({self.grado.nivel.nombre})"


from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Docente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con User
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.usuario.username})"
    

class DocenteDetalle(models.Model):
    docente = models.OneToOneField(Docente, on_delete=models.CASCADE, related_name="detalles")

    # 📅 Información personal
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email_institucional = models.EmailField(unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='docentes/', blank=True, null=True)  # Foto del docente

    # 📄 Documentos
    foto_dni = models.ImageField(upload_to='documentos/docentes/dni/', blank=True, null=True)
    curriculum_vitae = models.FileField(upload_to='documentos/docentes/cv/', blank=True, null=True)
    contrato = models.FileField(upload_to='documentos/docentes/contratos/', blank=True, null=True)

    # 📚 Información académica y laboral
    titulo_profesional = models.CharField(max_length=200, blank=True, null=True)
    especializacion = models.CharField(max_length=200, blank=True, null=True)
    institucion_egreso = models.CharField(max_length=200, blank=True, null=True)
    anios_experiencia = models.PositiveIntegerField(blank=True, null=True)
    cursos_asignados = models.ManyToManyField('Curso', blank=True)  # Relación con cursos

    # 📌 Información laboral
    tipo_contrato = models.CharField(
        max_length=50,
        choices=[('Tiempo Completo', 'Tiempo Completo'), ('Tiempo Parcial', 'Tiempo Parcial'), ('Contratado', 'Contratado')],
        default='Contratado'
    )
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_fin_contrato = models.DateField(null=True, blank=True)

    # 🏫 Datos institucionales
    codigo_docente = models.CharField(max_length=20, unique=True, blank=True, null=True)
    estado_docente = models.CharField(
        max_length=20,
        choices=[('Activo', 'Activo'), ('Licencia', 'Licencia'), ('Retirado', 'Retirado')],
        default='Activo'
    )

    # 👨‍👩‍👧‍👦 Contactos de emergencia
    contacto_emergencia = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto_emergencia = models.CharField(max_length=15, blank=True, null=True)
    parentesco_contacto = models.CharField(max_length=50, blank=True, null=True)

    # ⚕️ Datos médicos
    tipo_sangre = models.CharField(max_length=5, blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    enfermedades = models.TextField(blank=True, null=True)
    seguro_medico = models.CharField(max_length=100, blank=True, null=True)

    # 🌎 Información adicional
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    idiomas = models.CharField(max_length=100, blank=True, null=True, help_text="Ejemplo: Español, Inglés, Francés")

    def __str__(self):
        return f"Detalles de {self.docente.nombre} {self.docente.apellido}"
    
class TareaDocente(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='tareas')  # Relación con el docente
    descripcion = models.TextField()  # Descripción de la tarea
    fecha_entrega = models.DateField()  # Fecha de entrega de la tarea
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha en la que se asigna la tarea

    def __str__(self):
        return f"Tarea para {self.docente.nombre} {self.docente.apellido} - {self.fecha_entrega}"    


class AsistenciaDocente(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="asistencias")
    fecha = models.DateField(default=now)  # Registra la fecha automáticamente
    hora_ingreso = models.TimeField(blank=True, null=True)
    hora_salida = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = ('docente', 'fecha')  # Evita registros duplicados por día

    def registrar_salida(self):
        """Registra la hora de salida si aún no ha sido registrada."""
        if not self.hora_salida:
            self.hora_salida = now().time()
            self.save()

    @property
    def ha_marcado_salida(self):
        """Retorna True si el docente ya marcó su salida."""
        return self.hora_salida is not None

    def __str__(self):
        return f"Asistencia {self.docente.usuario.username} - {self.fecha}"




from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Cada alumno tiene un usuario
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    seccion = models.ForeignKey('Seccion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.seccion}"

    
class AlumnoDetalle(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, related_name="detalles")
    
    # 📅 Información personal
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)  # Teléfono del alumno
    imagen = models.ImageField(upload_to='alumnos/', blank=True, null=True)  # Foto del alumno

    # 📄 Documentos
    foto_dni = models.ImageField(upload_to='documentos/dni/', blank=True, null=True)
    partida_nacimiento = models.ImageField(upload_to='documentos/partidas/', blank=True, null=True)
    ficha_matricula = models.FileField(upload_to='documentos/matriculas/', blank=True, null=True)

    # 📚 Información académica
    codigo_estudiante = models.CharField(max_length=20, unique=True, blank=True, null=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    estado_academico = models.CharField(
        max_length=20,
        choices=[('Regular', 'Regular'), ('Condicional', 'Condicional'), ('Retirado', 'Retirado')],
        default='Regular'
    )

    # 👨‍👩‍👧‍👦 Contactos de emergencia
    nombre_padre = models.CharField(max_length=100, blank=True, null=True)
    telefono_padre = models.CharField(max_length=15, blank=True, null=True)
    nombre_madre = models.CharField(max_length=100, blank=True, null=True)
    telefono_madre = models.CharField(max_length=15, blank=True, null=True)
    nombre_tutor = models.CharField(max_length=100, blank=True, null=True)  # Si no es papá/mamá
    telefono_tutor = models.CharField(max_length=15, blank=True, null=True)

    # ⚕️ Datos médicos
    tipo_sangre = models.CharField(max_length=5, blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    enfermedades = models.TextField(blank=True, null=True)
    seguro_medico = models.CharField(max_length=100, blank=True, null=True)

    # 🌎 Información adicional
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    idiomas = models.CharField(max_length=100, blank=True, null=True, help_text="Ejemplo: Español, Inglés, Francés")

    # 🛑 Restricciones y autorizaciones
    salida_autorizada = models.BooleanField(default=True, help_text="¿Puede salir solo después de clases?")
    restricciones_legales = models.TextField(blank=True, null=True, help_text="Ejemplo: Orden judicial, tutoría legal")

    def __str__(self):
        return f"Detalles de {self.alumno.nombre} {self.alumno.apellido}"



class CursoAsignado(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.curso} - {self.seccion} (Prof. {self.docente})"

from django.db import models

from django.db import models
from datetime import datetime

from django.db import models
from django.utils import timezone

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="asistencias")
    curso_asignado = models.ForeignKey(CursoAsignado, on_delete=models.CASCADE, related_name="asistencias")
    fecha = models.DateField(default=timezone.now)  # Permite establecer la fecha manualmente
    hora = models.TimeField(default=timezone.now)  # Permite establecer la hora manualmente
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name="asistencias")
    estado = models.CharField(max_length=10, choices=[
        ('Presente', 'Presente'),
        ('Tarde', 'Tarde'),
        ('Ausente', 'Ausente')
    ], default='Presente')

    class Meta:
        unique_together = ('alumno', 'curso_asignado', 'fecha')  # Solo un registro por día por alumno

    def __str__(self):
        return f"{self.alumno} - {self.fecha} {self.hora}: {self.estado}"



# Modelo para representar trabajos asignados
class Trabajo(models.Model):
    curso_asignado = models.ForeignKey(CursoAsignado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_entrega = models.DateField()
    hora_entrega = models.TimeField(default=timezone.now)  # Hora límite de entrega
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    tipo_trabajo = models.CharField(max_length=50, choices=[
        ('Ensayo', 'Ensayo'),
        ('Investigación', 'Investigación'),
        ('Ejercicios', 'Ejercicios'),
        ('Proyecto', 'Proyecto'),
        ('Otro', 'Otro')
    ], default='Otro')
    es_obligatorio = models.BooleanField(default=True)  # Indica si el trabajo es obligatorio

    def __str__(self):
        obligatorio = "Obligatorio" if self.es_obligatorio else "Opcional"
        return f"{self.titulo} - {self.curso_asignado} ({self.fecha_entrega} {self.hora_entrega}) [{self.tipo_trabajo}] - {obligatorio}"


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Calificacion(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Revisado', 'Revisado'),
        ('Aprobado', 'Aprobado'),
    ]

    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name="calificaciones")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="calificaciones")
    curso_asignado = models.ForeignKey(CursoAsignado, on_delete=models.CASCADE, related_name="calificaciones")
    nota = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(20)], 
        help_text=_("Ingrese una nota entre 0 y 20.")
    )
    comentarios = models.TextField(blank=True, verbose_name=_("Comentarios del Docente"))
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"{self.alumno} - {self.trabajo} → Nota: {self.nota} ({self.estado})"



class Comportamiento(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    observacion = models.TextField()
    calificacion = models.CharField(max_length=20, choices=[
        ('Excelente', 'Excelente'),
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Deficiente', 'Deficiente')
    ])

    def __str__(self):
        return f"{self.alumno} - {self.fecha}: {self.calificacion}"

# Modelo para registrar exámenes
class Examen(models.Model):
    curso_asignado = models.ForeignKey(CursoAsignado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)  # Hora del examen
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    tipo_examen = models.CharField(max_length=50, choices=[
        ('Parcial', 'Parcial'),
        ('Final', 'Final'),
        ('Práctico', 'Práctico'),
        ('Otro', 'Otro')
    ], default='Parcial')

    def __str__(self):
        return f"{self.titulo} - {self.curso_asignado} ({self.fecha} {self.hora}) [{self.tipo_examen}]"


class Practica(models.Model):
    curso_asignado = models.ForeignKey(CursoAsignado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.curso_asignado} ({self.fecha})"

class CalificacionExamen(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"{self.alumno} - {self.examen}: {self.nota}"

class CalificacionPractica(models.Model):
    practica = models.ForeignKey(Practica, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"{self.alumno} - {self.practica}: {self.nota}"



from django.db import models

class EventoCalendario(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    tipo_evento = models.CharField(
        max_length=50,
        choices=[('Clase', 'Clase'), ('Examen', 'Examen'), ('Reunión', 'Reunión'), ('Otro', 'Otro')]
    )

    def __str__(self):
        return f"{self.titulo} - {self.fecha_inicio.strftime('%d/%m/%Y')}"


########Nuevas MODIFICACIONES############
from django.db import models
from ckeditor.fields import RichTextField

# class Unidad(models.Model):
#     curso = models.ForeignKey("Curso", on_delete=models.CASCADE, related_name="unidades")
#     nombre = models.CharField(max_length=100)
#     descripcion = RichTextField(blank=True, help_text="Descripción breve de la unidad")
#     numero = models.PositiveIntegerField(help_text="Número de la unidad dentro del curso")

#     class Meta:
#         ordering = ['numero']

#     def __str__(self):
#         return f"Unidad {self.numero}: {self.nombre} ({self.curso.nombre})"

from django.db import models
from ckeditor.fields import RichTextField  # Para descripciones enriquecidas

class Unidad(models.Model):
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE, related_name="unidades")
    nombre = models.CharField(max_length=100)
    descripcion = RichTextField(blank=True, help_text="Descripción breve de la unidad")
    numero = models.PositiveIntegerField(help_text="Número de la unidad dentro del curso")
    material_pdf = models.FileField(upload_to='unidades_pdfs/', blank=True, null=True)  # 📂 PDF
    video_url = models.URLField(blank=True, null=True, help_text="Enlace a video de YouTube")  # 🎥 Video

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f"Unidad {self.numero}: {self.nombre} ({self.curso.nombre})"


from django.db import models
from ckeditor.fields import RichTextField

class Tema(models.Model):
    unidad = models.ForeignKey(
        "Unidad",
        on_delete=models.CASCADE,
        related_name="temas",
        verbose_name="Unidad"
    )
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre del Tema"
    )
    descripcion = RichTextField(
        blank=True,
        help_text="Descripción detallada del tema con formato enriquecido",
        verbose_name="Descripción"
    )
    numero = models.PositiveIntegerField(
        help_text="Número del tema dentro de la unidad",
        verbose_name="Número"
    )

    class Meta:
        ordering = ["numero"]
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        unique_together = ("unidad", "numero")  # Evita que dos temas tengan el mismo número en una unidad

    def __str__(self):
        return f"Unidad {self.unidad.numero} - Tema {self.numero}: {self.nombre}"

    def get_absolute_url(self):
        return f"/temas/{self.id}/"  # Puedes modificarlo según tus rutas




class RecursoDidactico(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name="recursos")
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, help_text="Descripción breve del recurso")
    tipo = models.CharField(
        max_length=50,
        choices=[('Documento', 'Documento'), ('Video', 'Video'), ('Enlace', 'Enlace'), ('Otro', 'Otro')],
        default='Documento'
    )
    archivo = models.FileField(upload_to='recursos/', blank=True, null=True)
    enlace = models.URLField(blank=True, null=True, help_text="Enlace a un recurso externo")

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.tema.nombre}"

class Planificacion(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name="planificaciones")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    objetivos = models.TextField(help_text="Objetivos de la planificación")
    actividades = models.TextField(help_text="Descripción de las actividades a realizar")
    evaluacion = models.TextField(help_text="Criterios de evaluación")

    def __str__(self):
        return f"Planificación de {self.unidad.nombre} ({self.unidad.curso.nombre})"


from django.db import models

class HorarioDocente(models.Model):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
    ]

    docente = models.ForeignKey('Docente', on_delete=models.CASCADE)
    curso_asignado = models.ForeignKey('CursoAsignado', on_delete=models.CASCADE)
    dia = models.CharField(max_length=10, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    aula = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('docente', 'dia', 'hora_inicio', 'hora_fin')

    def __str__(self):
        return f"{self.docente} - {self.curso_asignado} - {self.dia} ({self.hora_inicio} - {self.hora_fin})"
