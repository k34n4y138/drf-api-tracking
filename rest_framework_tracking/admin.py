from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.html import format_html, escape

from .models import APIRequestLog


class APIRequestLogAdmin(admin.ModelAdmin):
    date_hierarchy = 'requested_at'
    list_display = ('id', 'requested_at', 'response_ms', 'status_code',
                    'user', 'method',
                    'path', 'remote_addr', 'host', 'browser', 'operating_system')
    list_filter = ('method', 'status_code',)
    search_fields = ('path', 'user__email', 'user__id',)
    readonly_fields = ('user_link',)
    exclude = ('user',)
    if getattr(settings, 'DRF_TRACKING_ADMIN_LOG_READONLY', False):
        readonly_fields = ('user', 'username_persistent', 'requested_at',
                           'response_ms', 'path', 'view', 'view_method',
                           'remote_addr', 'host', 'method', 'query_params',
                           'data', 'response', 'errors', 'status_code', 'browser', 'operating_system', 'user_link',
                           'user_agent')

    def user_link(self, obj):
        if obj.user.is_authenticated:
            return
        ct = ContentType.objects.get_for_model(obj.user.model)
        if not ct:
            return
        return format_html('<a href="%s">%s</a>' % (
            reverse("admin:%s_%s_change" % (ct.app_label, ct.model), args=(obj.user.id,)), escape(obj.user)))

    user_link.allow_tags = True
    user_link.short_description = "User"

    def has_delete_permission(self, request, obj=None):
        if getattr(settings, 'DRF_TRACKING_ADMIN_LOG_READONLY', False):
            return False

        return super(APIRequestLogAdmin, self).has_delete_permission(request, obj)


admin.site.register(APIRequestLog, APIRequestLogAdmin)
