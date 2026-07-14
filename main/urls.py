from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("videos/", views.videos, name="videos"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
]