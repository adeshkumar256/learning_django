from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=500)
    # null True if it can have null value or not
    author = models.CharField(null=True, max_length=100)
    # id = models.AutoField() no need as model will automatically create

    def get_absolute_url(self):
        return reverse("post-details", args=[self.id])

    def __str__(self):
        return f"{self.title} {self.rating} {self.description}"
