from django import forms

from russian_fields import validators

class KPPField(forms.CharField):
    default_validators = [validators.kpp_validator]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(KPPField, self).clean(value)


class INNField(forms.CharField):
    default_validators = [validators.inn_validator]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(INNField, self).clean(value)


class OGRNField(forms.CharField):
    default_validators = [validators.ogrn_validator]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(OGRNField, self).clean(value)


class PhoneNumberField(forms.CharField):
    default_validators = [validators.phone_validator]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(PhoneNumberField, self).clean(value)


class PercentField(forms.IntegerField):
    def to_python(self, value):
        if value and isinstance(value, basestring) and value[-1] == '%':
            value = value[:-1]
        return super(PercentField, self).to_python(value)

    def clean(self, value):
        return super(PercentField, self).clean(value)