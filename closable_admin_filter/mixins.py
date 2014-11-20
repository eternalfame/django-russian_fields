from django.conf import settings
from django.contrib.admin import ModelAdmin


class AdminClosableFilterMixin(ModelAdmin):
    class Media:
        js = [settings.STATIC_URL + 'admin/js/admin_filter_closable.js']
