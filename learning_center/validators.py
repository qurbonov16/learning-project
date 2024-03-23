from django.core.exceptions import ValidationError
import phonenumbers
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    num = phonenumbers.parse(str(value))
    if not phonenumbers.is_valid_number(num):
        raise ValidationError('The phone number is not correct ! Please try again.')


def full_name(value):
    x = value.split(" ")
    if len(x) < 2:
        raise ValidationError(_('The full name must be 3 words !'), code='invalid_full_name')


def address(value):
    x = value.split(" ")
    if len(x) < 3:
        raise ValidationError(_('The address must be 3 words !'), code='invalid_location')