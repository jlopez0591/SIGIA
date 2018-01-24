from perfiles.models import Person
from dal import autocomplete


class PerfilAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = Person.objects.all()
        else:
            return Person.objects.none()

        if self.q:
            qs = qs.filter(
                nombre_completo__icontains=self.q
            )
        return qs