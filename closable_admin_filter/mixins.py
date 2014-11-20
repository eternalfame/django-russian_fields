from django.conf import settings
from django.contrib.admin import ModelAdmin


class AdminClosableFilterMixin(ModelAdmin):
    class Media:
        css = {
            'screen': (
                settings.STATIC_URL + '/admin/css/closable_admin_filter.css',
            )
        }
        js = (
            settings.STATIC_URL + 'admin/js/closable_admin_filter.js',
        )
