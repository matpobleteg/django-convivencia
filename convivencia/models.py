from django.db import models

# Create your models here.
from django.urls import reverse


class ResponsableAlumno(models.Model):
    nombre = models.CharField(max_length=255)
    relacion_parentesco = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse('responsable_detail', args=[str(self.id)])


class Alumno(models.Model):
    # Alumno Info.
    nombre_alumno = models.CharField(max_length=255)
    apellido_alumno = models.CharField(max_length=255)
    rut_alumno = models.CharField(max_length=255)
    dv_alumno = models.CharField(max_length=255)
    fecha_nacimiento_alumno = models.DateField()
    apoderado_alumno = models.OneToOneField(ResponsableAlumno, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_alumno} {self.apellido_alumno}'

    def get_absolute_url(self):
        return reverse('alumno_detail', args=[str(self.id)])

    # Establecimiento
    # ...

    # Caso Vulneracion de Derechos


class CasoVulneracionDerechos(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    maltrato_fisico = models.CharField(max_length=255)
    maltrato_emocional = models.CharField(max_length=255)
    abuso = models.CharField(max_length=255)
    abandono_negligencia = models.CharField(max_length=255)
    fecha_caso = models.DateField()

    def __str__(self):
        return f'{self.id} - caso de: {self.alumno}'


class Maltrato(models.Model):
    caso_vulneracion = models.ForeignKey(CasoVulneracionDerechos, on_delete=models.CASCADE)
    tipo_maltrato = models.CharField(max_length=255)
    antecedentes = models.CharField(max_length=255)


class Discriminacion(models.Model):
    caso_vulneracion = models.ForeignKey(CasoVulneracionDerechos, on_delete=models.CASCADE)
    tipo_discrim = models.CharField(max_length=255)


class Medidas(models.Model):
    tipo_medida = models.CharField(max_length=255)
    caso_maltrato = models.ForeignKey(Maltrato, on_delete=models.CASCADE, null=True)
    caso_discrim = models.ForeignKey(Discriminacion, on_delete=models.CASCADE, null=True)