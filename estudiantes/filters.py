from estudiantes.models import Estudiante
from estudiantes.forms import EstudianteFilterForm

import django_filters as df


class EstudianteFilter(df.FilterSet):
    class Meta:
        model = Estudiante
        fields = ['provincia', 'clase', 'tomo', 'folio']