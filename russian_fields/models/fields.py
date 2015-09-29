from django.db.models import fields
from russian_fields import fields as formfields
from russian_fields import validators

__all__ = ('INNField', "KPPField", "OGRNField", "PhoneNumberField")


class KPPField(fields.CharField):
    default_validators = [validators.kpp_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 9)
        super(KPPField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'varchar(%s)' % self.max_length

    def get_internal_type(self):
        return "KPPField"

    def formfield(self, **kwargs):
        defaults = {'form_class': formfields.KPPField}
        defaults.update(kwargs)
        return super(KPPField, self).formfield(**defaults)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect the _actual_ field.
        from south.modelsinspector import introspector
        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        args, kwargs = introspector(self)
        # That's our definition!PercentField
        return field_class, args, kwargs


class INNField(fields.CharField):
    default_validators = [validators.inn_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 12)
        super(INNField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'varchar(%s)' % self.max_length

    def get_internal_type(self):
        return "INNField"

    def formfield(self, **kwargs):
        defaults = {'form_class': formfields.INNField}
        defaults.update(kwargs)
        return super(INNField, self).formfield(**defaults)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect the _actual_ field.
        from south.modelsinspector import introspector
        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        args, kwargs = introspector(self)
        # That's our definition!
        return field_class, args, kwargs


class OGRNField(fields.CharField):
    default_validators = [validators.ogrn_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 13)
        super(OGRNField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'varchar(%s)' % self.max_length

    def get_internal_type(self):
        return "OGRNField"

    def formfield(self, **kwargs):
        defaults = {'form_class': formfields.OGRNField}
        defaults.update(kwargs)
        return super(OGRNField, self).formfield(**defaults)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect the _actual_ field.
        from south.modelsinspector import introspector
        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        args, kwargs = introspector(self)
        # That's our definition!
        return field_class, args, kwargs


class PhoneNumberField(fields.CharField):
    default_validators = [validators.phone_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 30)
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'varchar(%s)' % self.max_length

    def get_internal_type(self):
        return "PhoneNumberField"

    def formfield(self, **kwargs):
        defaults = {'form_class': formfields.PhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect the _actual_ field.
        from south.modelsinspector import introspector
        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        args, kwargs = introspector(self)
        # That's our definition!
        return field_class, args, kwargs