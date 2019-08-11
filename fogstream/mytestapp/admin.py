from django.contrib import admin

from .models import UserMessage

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'text', 'status_text']
    def status_text(self, obj):
        if obj.status == 0:
            return "Отправлено."
        else:
            return "Не удалось отправить."

admin.site.register(UserMessage, UserMessageAdmin)

