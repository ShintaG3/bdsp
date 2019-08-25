from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('details/<id>', views.details, name="details"),
    path('editPage/<id>', views.editPage, name="editPage"),
    path('accounts/profile/', views.index, name="index"),
    path('search', views.search, name="search")
]
