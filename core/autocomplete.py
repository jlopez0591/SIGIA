from django.contrib.auth.models import User
from dal import autocomplete


class PerfilAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = User.objects.all()
        else:
            return User.objects.none()

        if self.q:
            qs = qs.filter(
                username__icontains=self.q
            )
        return qs