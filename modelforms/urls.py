from django.urls import path
from . import views

urlpatterns = [
    path("", views.model_forms, name="model_forms"),
]
