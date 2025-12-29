from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    
class CuerpoPertenencia(models.Model):
    class TipoCuerpo(models.TextChoices):
        COSTALEROS = 'COSTALEROS', 'Costaleros'
        NAZARENOS = 'NAZARENOS', 'Nazarenos'
        DIPUTADOS_TRAMO = 'DIPUTADOS_TRAMO', 'Diputados de tramo'
        BRAZALETES = 'BRAZALETES', 'Brazaletes'
        ACOLITOS = 'ACOLITOS', 'Cuerpo de acólitos'
        CAPATACES = 'CAPATACES', 'Capataces'
        SANITARIOS = 'SANITARIOS', 'Sanitarios'
        PRIOSTIA = 'PRIOSTIA', 'Priostía'
        CARIDAD_ACCION_SOCIAL = 'CARIDAD', 'Caridad y acción social'
        JUVENTUD = 'JUVENTUD', 'Juventud'
        JUNTA_GOBIERNO = 'JUNTA_GOBIERNO', 'Junta de gobierno'

    nombre_cuerpo = models.CharField(
        max_length=50,
        choices=TipoCuerpo.choices,
        unique=True,
        verbose_name="Nombre del cuerpo",
        null=True,  # <--- Añade esto temporalmente
        blank=True  # <--- Añade esto temporalmente
    )

    def __str__(self):
        return self.get_nombre_cuerpo_display()
    
class Hermano(models.Model):

    class EstadoHermano(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        BAJA = 'BAJA', 'Baja'

    class EstadoPago(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente de pago'
        PAGADA = 'PAGADA', 'Pagada'
        EXENTO = 'EXENTO', 'Exento de pago'

    numero_registro = models.IntegerField(unique=True, primary_key=True, verbose_name = "Número de registro")
    nombre = models.CharField(max_length=100, verbose_name = "Nombre")
    primer_apellido = models.CharField(max_length=100, verbose_name = "Primer apellido")
    segundo_apellido = models.CharField(max_length=100, verbose_name = "Segundo apellido")
    dni = models.CharField(max_length=9, unique=True, verbose_name = "DNI")
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de nacimiento")
    direccion_postal = models.CharField(max_length=255, verbose_name = "Dirección postal")
    codigo_postal = models.CharField(max_length=5, verbose_name = "Código postal")
    telefono = models.CharField(max_length=9, verbose_name = "Teléfono")
    correo_electronico = models.EmailField(unique=True, verbose_name = "Correo electrónico")

    nombre_usuario = models.CharField(max_length=50, unique=True, verbose_name = "Nombre de usuario")
    contrasena = models.CharField(max_length=128, verbose_name = "Contraseña")
    fecha_alta = models.DateField(auto_now_add=True, verbose_name = "Fecha de alta")

    estado_hermano = models.CharField(
        max_length = 10,
        choices = EstadoHermano.choices,
        default = EstadoHermano.ACTIVO,
        verbose_name = "Estado del hermano"
    )

    estado_pago = models. CharField(
        max_length = 20,
        choices = EstadoPago.choices,
        default=EstadoPago.PENDIENTE,
        verbose_name = "Estado de pago"
    )

    es_admin = models.BooleanField(default=False, verbose_name = "Es administrador")

    cuerpos = models.ManyToManyField(
        CuerpoPertenencia,
        related_name='hermanos',
        verbose_name="Cuerpos de pertenencia",
        blank=True
    )

    areas_interes = models.ManyToManyField(
        'AreaInteres',
        related_name='hermanos',
        verbose_name="Áreas de interés",
        blank=True
    )

    def __str__(self):
        return f"{self.numero_registro} - {self.nombre} {self.primer_apellido}"
    
class PapeletaSitio(models.Model):
    class EstadoPapeleta(models.TextChoices):
        NO_SOLICITADA = 'NO_SOLICITADA', 'No solicitada'
        SOLICITADA = 'SOLICITADA', 'Solicitada'
        EMITIDA = 'EMITIDA', 'Emitida'
        RECOGIDA = 'RECOGIDA', 'Recogida'
        LEIDA = 'LEIDA', 'Leída'
        ANULADA = 'ANULADA', 'Anulada'

    numero_papeleta = models.AutoField(primary_key=True, verbose_name = "Número de papeleta")
    estado_papeleta = models.CharField(
        max_length = 20,
        choices = EstadoPapeleta.choices,
        default = EstadoPapeleta.NO_SOLICITADA,
        verbose_name = "Estado de la papeleta"
    )

    fecha_emision = models.DateTimeField(null=True, blank=True, verbose_name = "Fecha de emisión")
    codigo_verificacion = models.CharField(max_length=100, unique=True, verbose_name = "Código de verificación")
    anio = models.IntegerField(verbose_name = "Año")
    lugar_citacion = models.CharField(max_length=255, verbose_name="Lugar de citación")
    hora_citacion = models.TimeField(verbose_name="Hora de citacion")

    hermano = models.ForeignKey(
        'Hermano',
        on_delete=models.CASCADE,
        related_name='papeletas',
        verbose_name="Hermano"
    )

    acto = models.ForeignKey(
        'Acto',
        on_delete=models.PROTECT,
        related_name='papeletas_generadas',
        verbose_name="Acto",
        null=True,
        blank=True
    )

    puesto = models.ForeignKey(
        'Puesto',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='papeletas_asignadas',
        verbose_name="Puesto"
    )

    def __str__(self):
        return f"Papeleta {self.numero_papeleta} - {self.get_estado_papeleta_display()}"
    
class Comunicado(models.Model):
    class TipoComunicacion(models.TextChoices):
        ACUERDO_CABILDO = 'ACUERDO_CABILDO', 'Acuerdos de cabildos'
        CONVOCATORIA_CABILDO = 'CONVOCATORIA_CABILDO', 'Convocatorias de cabildo'
        NOTICIA = 'NOTICIA', 'Noticias'
        COMUNICADO = 'COMUNICADO', 'Comunicados'
        FOTOGALERIA = 'FOTOGALERIA', 'Fotogalería'

    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de emisión")

    tipo_comunicacion = models.CharField(
        max_length=30,
        choices=TipoComunicacion.choices,
        default=TipoComunicacion.NOTICIA,
        verbose_name="Tipo de comunicación"
    )

    autor = models.ForeignKey(
        'Hermano', 
        on_delete=models.PROTECT,
        related_name='comunicados',
        verbose_name="Autor"
    )

    destinatarios = models.ManyToManyField(
        'AreaInteres',
        related_name='comunicados_recibidos',
        verbose_name="Áreas destinatarias",
        help_text="Seleccione las áreas de interés a las que va dirigido este comunicado"
    )

    def __str__(self):
        return f"{self.get_tipo_comunicacion_display()}: {self.titulo}"

class AreaInteres(models.Model):
    class TipoArea(models.TextChoices):
        CARIDAD = 'CARIDAD', 'Caridad'
        CULTOS_FORMACION = 'CULTOS_FORMACION', 'Cultos y Formación'
        JUVENTUD = 'JUVENTUD', 'Juventud (Grupo Joven)'
        PATRIMONIO = 'PATRIMONIO', 'Patrimonio'
        PRIOSTIA = 'PRIOSTIA', 'Priostía'
        DIPUTACION_MAYOR_GOBIERNO = 'DIPUTACION MAYOR GOBIERNO', 'Diputación mayor de gobierno'
        COSTALEROS = 'COSTALEROS', 'Costaleros'
        ACOLITOS = 'ACOLITOS', 'Cuerpo de acólitos'

    nombre = models.CharField(
        max_length=50,
        choices=TipoArea.choices,
        unique=True,
        verbose_name="Nombre del área"
    )

    def __str__(self):
        return self.get_nombre_display()
    
class Acto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del acto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    fecha = models.DateField(verbose_name="Fecha del acto")
    tipo_acto = models.ForeignKey(
        'TipoActo', 
        on_delete=models.PROTECT, 
        related_name='actos',
        verbose_name="Tipo de acto"
    )

    def __str__(self):
        return f"{self.nombre} - {self.tipo_acto.get_nombre_display()} ({self.fecha.year})"
    
class Puesto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del puesto")
    tipo = models.CharField(max_length=50, verbose_name="Tipo (Tramo, Insignia, etc.)")
    numero_maximo_asignaciones = models.PositiveIntegerField(verbose_name="Máximo de asignaciones")
    disponible = models.BooleanField(default=True, verbose_name="¿Está disponible?")
    
    acto = models.ForeignKey(
        'Acto',
        on_delete=models.CASCADE,
        related_name='puestos',
        verbose_name="Acto"
    )

    def __str__(self):
        return f"{self.nombre} - {self.acto.nombre}"
    
class TipoActo(models.Model):
    class Tipo(models.TextChoices):
        ESTACION_PENITENCIA = 'ESTACION_PENITENCIA', 'Estación de Penitencia'
        CABILDO_GENERAL = 'CABILDO_GENERAL', 'Cabildo General de Hermanos'
        CABILDO_EXTRAORDINARIO = 'CABILDO_EXTRAORDINARIO', 'Cabildo Extraordinario de Hermanos'
        VIA_CRUCIS = 'VIA_CRUCIS', 'Vía Crucis'
        QUINARIO = 'QUINARIO', 'Quinario'
        TRIDUO = 'TRIDUO', 'Triduo'
        ROSARIO_AURORA = 'ROSARIO_AURORA', 'Rosario de la Aurora'
        CONVIVENCIA = 'CONVIVENCIA', 'Convivencia'

    tipo = models.CharField(max_length=100, unique=True, choices = Tipo.choices, verbose_name="Nombre del tipo de acto")
    requiere_papeleta = models.BooleanField(default=True, verbose_name="¿Requiere papeleta de sitio?")
    
    cuerpos_requeridos = models.ManyToManyField(
        'CuerpoPertenencia',
        related_name='tipos_acto_permitidos',
        verbose_name="Cuerpos requeridos/permitidos",
        blank=True
    )

    def __str__(self):
        return self.get_tipo_display()