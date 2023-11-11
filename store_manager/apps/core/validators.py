from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext as _


def validate_dni(value):
    if len(value) < 7 and len(value) > 8:
        raise ValidationError(
            _('El dni debe tener 8 digitos.'),
            code='invalid_dni'
        )

def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(
            _('Este campo solo debe contener letras.'),
            code='invalid_input'
        )
        
def validate_birth_date(value):
    today = timezone.now().date()
    if (today-value).days < 6570:
        raise ValidationError(
            _('La persona debe ser mayor de edad.'),
            code='invalid_birthdate'
        )