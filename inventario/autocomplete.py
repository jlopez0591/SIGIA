from dal import autocomplete

from inventario.models import Categoria, Fabricante, Modelo


class FabricanteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            qs = Fabricante.objects.all()
        else:
            return Fabricante.objects.none()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)
        return qs


class CategoriaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            qs = Categoria.objects.all()
        else:
            return Categoria.objects.none()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)
        return qs


class ModeloAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            qs = Modelo.objects.all()
        else:
            return Modelo.objects.none()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)
        return qs
