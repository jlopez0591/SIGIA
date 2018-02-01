import os
import magic
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError


def validate_file_type(upload):
    """
    Valida que los archivos cargados sean en formato PDF.
    :param upload:
    :return: True o False
    """
    # Guardar archivos para el analisis en /tmp
    tmp_path = 'tmp/{}'.format(upload.name)
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)

    # Obtener el tipo de MIME del archivo utilizando python-magic y eliminar el archivo
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)

    if file_type not in 'application/pdf':  # TODO: Verificar este pedazo
        raise ValidationError('Tipo de archivo no soportado, solo aceptamos .PDF')
