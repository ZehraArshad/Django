from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.contact, name="contact")
]