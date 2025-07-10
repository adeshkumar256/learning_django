from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40)


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, ({self.postal_code})"

    class Meta:
        # plural enteries in model then this will visible on admin portal
        verbose_name_plural = "Address Enteries"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    # in one to one it will not be author_set it will be author

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Post(models.Model):
    # id = models.AutoField() no need as model will automatically create
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=500)
    # null True if it can have null value or not
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="posts")
    # relative name for one to many relationship
    slug = models.SlugField(default="", blank=True, null=False,
                            db_index=True)  # for indexing
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-details", args=[self.slug])

    # Overwrite built in save method so that slug can be form
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)  # make sure built in save is called

    # no need to overwrite save function as now we are using admin models to configure the fields

    def __str__(self):
        return f"{self.title} {self.rating} {self.description} {self.slug}"
