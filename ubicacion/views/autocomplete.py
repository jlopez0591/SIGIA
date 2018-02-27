from dal import autocomplete
from ubicacion.models import CarreraInstancia, SeccionInstancia, Sede, UnidadInstancia, Unidad, Seccion, Carrera


class CarreraInstanciaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = CarreraInstancia.objects.all()
        elif self.request.user.is_authenticated():
            qs = CarreraInstancia.objects.all()
        else:
            return CarreraInstancia.objects.none()

        if self.q:
            qs = qs.filter(nombre_proyecto__icontains=self.q)
        return qs
