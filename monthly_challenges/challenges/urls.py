from django.urls import path
from . import views

urlpatterns = [
    # url to show All challenges
    path("", views.index),
    # Dynamic url that handles int
    path("<int:month>", views.monthly_challenge_by_number),
    # Dynamic url that handles strings
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
