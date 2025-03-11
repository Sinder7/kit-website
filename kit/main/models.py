from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.JSONField(default=list, blank=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="subpages"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


BLOCK_TYPES = [("text", "Текст"), ("image", "Изображение"), ("video", "Видео")]


class PageBlock(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="blocks")
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES)
    content = models.TextField(blank=True)
    order = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ["order"]


    def __str__(self):
        return f"{self.page.title} - {self.get_block_type_display()}"
    
    