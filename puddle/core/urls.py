from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns = [
    path("contact/", views.contact, name="contact")
]