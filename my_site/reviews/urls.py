from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewView.as_view(), name="reviews"),
    path("thank-you", views.ThankView.as_view(), name="thank-you"),
    path("list", views.ReviewListView.as_view(), name="review-list"),
    path("/review/<int:id>", views.SingleReviewView.as_view(), name="review")
]
