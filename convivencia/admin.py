from django.contrib import admin
from .models import Alumno, ResponsableAlumno, CasoVulneracionDerechos, Maltrato, Discriminacion, Medidas


# Register your models here.

class CasoVulneracionDerechosInline(admin.TabularInline):
    model = CasoVulneracionDerechos


class AlumnoAdmin(admin.ModelAdmin):
    inlines = [
        CasoVulneracionDerechosInline,
    ]
    list_display = ('nombre_alumno', 'apellido_alumno', 'apoderado_alumno')


admin.site.register(Alumno, AlumnoAdmin)


class ResponsableAlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alumno', 'relacion_parentesco')


admin.site.register(ResponsableAlumno, ResponsableAlumnoAdmin)


class CasoVulneracionDerechosAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'fecha_caso')


admin.site.register(CasoVulneracionDerechos, CasoVulneracionDerechosAdmin)

admin.site.register(Maltrato)
admin.site.register(Discriminacion)
admin.site.register(Medidas)
