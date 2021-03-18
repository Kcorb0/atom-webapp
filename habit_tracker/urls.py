from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='atom-home'),
    path('help/', views.app_help, name='atom-help'),
]