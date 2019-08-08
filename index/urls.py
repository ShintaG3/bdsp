from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('organization/', views.organization, name='organization'),
    path('service/', views.service, name='service'),
    path('detail/', views.detail, name='detail'),
]
