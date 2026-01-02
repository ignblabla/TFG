from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="notes"
    )

    def __str__(self):
        return self.title
    
class Hermano(AbstractUser):

    class EstadoHermano(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        BAJA = 'BAJA', 'Baja'

    class EstadoPago(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente de pago'
        PAGADA = 'PAGADA', 'Pagada'
        EXENTO = 'EXENTO', 'Exento de pago'

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=100, verbose_name = "Nombre")
    primer_apellido = models.CharField(max_length=100, verbose_name = "Primer apellido")
    segundo_apellido = models.CharField(max_length=100, verbose_name = "Segundo apellido")
    dni = models.CharField(max_length=9, unique=True, verbose_name = "DNI")

    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name = "Fecha de ingreso")

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

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombre', 'primer_apellido', 'segundo_apellido', 'email']

    def __str__(self):
        return f"{self.numero_registro} - {self.nombre} {self.primer_apellido}"
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.dni
        super().save(*args, **kwargs)