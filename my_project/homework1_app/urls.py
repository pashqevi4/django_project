from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_homepage, name='homepage'),
    path('about/', views.get_about, name='about'),
]
