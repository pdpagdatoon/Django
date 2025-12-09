from django.contrib import admin
from .models import AdminComment


@admin.register(AdminComment)
class AdminCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "comment")
    readonly_fields = ("user", "created_at", "comment")

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
