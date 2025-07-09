from django.contrib import admin

from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author")  # filters
    # to configure what to show in admin table previouslt the __str__ output was showing
    list_display = ("title", "author")


admin.site.register(Post, PostAdmin)
