from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError("O tamanho máximo de arquivo que pode ser enviado é de 10 MB")
    else:
        return value
