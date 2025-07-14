from . import views
from django.urls import path

urlpatterns = [
    path("", views.review, name="reviews"),
    path("thank-you", views.thank_you, name="thank-you")
]
