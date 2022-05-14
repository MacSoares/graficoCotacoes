from django.urls import path
from graph import views

urlpatterns = [
    path('', views.home, name='home'),
]
