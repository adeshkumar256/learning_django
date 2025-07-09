from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    # id = models.AutoField() no need as model will automatically create
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=500)
    # null True if it can have null value or not
    author = models.CharField(null=True, max_length=100)
    slug = models.SlugField(default="", blank=True, null=False,
                            db_index=True)  # for indexing

    def get_absolute_url(self):
        return reverse("post-details", args=[self.slug])

    # Overwrite built in save method so that slug can be form
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)  # make sure built in save is called

    def __str__(self):
        return f"{self.title} {self.rating} {self.description} {self.slug}"
