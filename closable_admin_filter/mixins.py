from django.conf import settings
from django.contrib.admin import ModelAdmin


class AdminClosableFilterMixin(ModelAdmin):
    class Media:
        js = [
            settings.STATIC_URL + 'admin/js/closable_admin_filter.js',
        ]
