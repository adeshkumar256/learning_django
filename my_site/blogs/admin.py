from django.contrib import admin

from .models import Post, Author

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author")  # filters
    # to configure what to show in admin table previouslt the __str__ output was showing
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
