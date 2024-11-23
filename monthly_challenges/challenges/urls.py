from django.urls import path
from . import views

urlpatterns = [
    # Dinamic url that handles int
    path("<int:month>", views.monthly_challenge_by_number),
    # Dinamic url that handles strings
    path("<str:month>", views.monthly_challenge)
]
