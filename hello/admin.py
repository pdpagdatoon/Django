from django.contrib import admin
from .models import AdminComment
from .models import Product
from .models import Feedback


# Admin to admin comment panel - Patrick David Pagdatoon
@admin.register(AdminComment)
class AdminCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "comment")
    readonly_fields = ("user", "created_at", "comment")

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, ProductAdmin)

from .models import Feedback


# User feedback form to Admin Panel - Patrick David Pagdatoon
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'short_message')
    readonly_fields = ('message', 'created_at')

    def short_message(self, obj):
        return obj.message[:50]  # preview first 50 chars

    short_message.short_description = "Message"
