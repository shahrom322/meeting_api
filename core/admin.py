from django.contrib import admin

from core.models import CustomUser


@admin.register(CustomUser)
class VisitorAdmin(admin.ModelAdmin):
    pass
