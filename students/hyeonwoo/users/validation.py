import json
import re

from django.core.exceptions import ValidationError
from django.http        import JsonResponse

def validate_email(value):
    email_regex = re.compile('^[a-zA-z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$')
    email_regex_2 = re.compile('^/\s/g')

    if email_regex_2.match(value):
        raise ValidationError('NO_VALUE')

    if not email_regex.match(value):
        raise ValidationError('INVALID_EMAIL_ADDREASS')

def validate_password(value):
    password_regex = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
    password_regex_2 = re.compile('^/\s/g')

    if password_regex_2.match(value):
        raise ValidationError('NO_VALUE')

    if not password_regex.match(value):
        raise ValidationError('INVALID_PASSWORD')