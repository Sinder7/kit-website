from django.contrib import admin
from .models import Page, PageBlock
from django.utils.html import format_html


class PageBlockInline(admin.TabularInline):
    model = PageBlock
    extra = 1
    fields = ("block_type", "text_content", "image", "video_url", "order", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="auto"/>', obj.image.url
            )
        return "Нет изображения"


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "parent")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PageBlockInline]
