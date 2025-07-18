from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email", "rating")


admin.site.register(Review, ReviewAdmin)
