from django.urls import path
from . import views  # . means from same folder and views means from views.py

# urlpatterns is standary list for defining urls in Django
#  we define a ULConfig so we have to use this in main project setup

# urlpatterns = [
#     path("january", views.jan),
#     path("february", views.feb),
# ]

urlpatterns = [
    # here the sequece is important if its convertible as int can be converted to string then int route should be at top
    path("", views.challenges),  # /challenges
    path("<int:month>", views.monthly_challenge_int),
    # named path
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
