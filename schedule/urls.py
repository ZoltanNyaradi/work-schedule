from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedule2, name="schedule"),
]