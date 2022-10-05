from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("muku", views.muku, name="muku"),
    path("jane", views.jane, name="jane"),
    path("<str:name>", views.greet, name="greet"),
]
