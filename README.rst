=====
Closable Admin Filter
=====

When there are too many fields in Django admin and it's necessary to have the filter, it turns to very ugly situation, when filter `flies` over the fields.

So here's a simple Django app to provide a "HIDE" button for the filter.

Quick start
-----------

1. Install the package using::

    pip install django-closable_admin_filter

2. Add "closable_admin_filter" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'closable_admin_filter',
    )

3. Add the AdminClosableFilterMixin to your inherited from ModelAdmin class like this::

	class MyAdmin(AdminClosableFilterMixin, admin.ModelAdmin):
		...

4. Visit http://your.domain/admin/your_app/your_model/ to enjoy the result.
