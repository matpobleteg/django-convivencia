from django.urls import path

from convivencia.views import AlumnoListView, AlumnoDetailView, ResponsableDetail

urlpatterns = [
    path('', AlumnoListView.as_view(), name='alumno_list'),
    path('<int:pk>', AlumnoDetailView.as_view(), name='alumno_detail'),
    path('responsable/<int:pk>', ResponsableDetail.as_view(), name='responsable_detail'),

]
