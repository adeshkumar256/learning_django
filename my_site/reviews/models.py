from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator, MaxLengthValidator

# Create your models here.


class Review(models.Model):
    user_name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        validators=[MinLengthValidator(8), MaxLengthValidator(100)])
    email = models.EmailField(null=False)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
