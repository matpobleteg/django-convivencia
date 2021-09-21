from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from convivencia.models import Alumno, ResponsableAlumno


class AlumnoListView(ListView):
    model = Alumno
    context_object_name = 'alumno_list'
    template_name = 'convivencia/alumno_list.html'


class AlumnoDetailView(DetailView):
    model = Alumno
    context_object_name = 'alumno'
    template_name = 'convivencia/alumno_detail.html'


class ResponsableDetail(DetailView):
    model = ResponsableAlumno
    template_name ='convivencia/responsable_detail.html'