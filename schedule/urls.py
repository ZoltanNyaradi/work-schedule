from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedule, name="schedule"),
]