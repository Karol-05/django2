from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on", "status")
    list_filter = ("status",)
    list_display_links = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    view_on_site = True
