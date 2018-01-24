from perfiles.models import Perfil
import django_filters as df


class PerfilFilter(df.FilterSet):
    class Meta:
        model = Perfil
        fields = ['provincia', 'clase', 'tomo', 'folio']
