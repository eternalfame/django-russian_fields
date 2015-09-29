# coding=utf-8
import re

from django.core.exceptions import ValidationError


def kpp_validator(value):
    errors = []
    if len(value) < 9:
        errors.append(u'Значение должно быть не короче 9 символов')
    if not value.isdigit():
        errors.append(u'Поле должно содержать только цифры')
    if errors:
        raise ValidationError(errors)


def inn_validator(value):
    def inn_csum(value):
        k = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
        pairs = zip(k[11-len(value):], [int(x) for x in value])
        return str(sum([k * v for k, v in pairs]) % 11 % 10)

    inn_length = len(value)
    if inn_length not in (10, 12):
        raise ValidationError(u'Должно быть введено 10 или 12 цифр')
    elif inn_length == 10:
        if value[-1] != inn_csum(value[:-1]):
            raise ValidationError(u'Введен некорректный ИНН')
    elif inn_length == 12:
        if value[-2:] != inn_csum(value[:-2]) + inn_csum(value[:-1]):
            raise ValidationError(u'Введен некорректный ИНН')


def ogrn_validator(value):
    errors = []
    if len(value) not in (13, 15):
        errors.append(u'Должно быть введено 13 (ОГРН) или 15 (ОГРНИП) цифр')
    if not value.isdigit():
        errors.append(u'Поле должно содержать только цифры')

    if errors:
        raise ValidationError(errors)

    if value[-1] != str(int(value[:-1]) % (len(value) - 2))[-1]:
        raise ValidationError(u'Введен некорректный ОГРН/ОГРНИП')


def phone_validator(value):
    errors = []
    if re.findall('[a-zA-Zа-яА-я]', value, re.UNICODE):
        errors.append(u'Поле не должно содержать буквы')
    if not re.match('^(\+7[\- ]?)(\(?\d{3,4}\)?[\- ]?)?[\d\- ]{6,10}$', value, re.UNICODE) or not len(re.sub('\D', '', value)) == 11:
        errors.append(u'Номер должен начинаться с +7 и содержать 11 цифр')
    if errors:
        raise ValidationError(errors)