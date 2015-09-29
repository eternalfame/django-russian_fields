=====
Django Russian Fields
=====

Приложение содержит поля, специфичные для разработки в российских условиях.

Список полей::

* INNField
* KPPField
* OGRNField
* PhoneNumberField

Инструкция
-----------

1. Установите пакет с помощью pip::

    pip install django-russian_fields

2. Добавьте "russian_fields" в INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'russian_fields',
    )

3. Импортируйте нужное поле в ваш models.py::

    from russian_fields.models.fields import INNField

4. Используйте импортированное поле в вашей модели::

    class MyModel(models.Model):
        ...
	inn = INNField(verbose_name=u"ИНН")

5. Радуйтесь!