from django.contrib import admin
from core.models import WriteUp, Project, ProjectImage


@admin.register(WriteUp)
class WriteUpAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "is_visible")
    search_fields = ("title", "description")
    list_filter = ("is_visible",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description", "created_at", "is_visible")
    search_fields = ("name", "short_description")
    list_filter = ("is_visible",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ProjectImage)
