from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('details/<name>', views.details, name="details")
]
