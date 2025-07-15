from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewView.as_view(), name="reviews"),
    path("thank-you", views.thank_you, name="thank-you")
]
