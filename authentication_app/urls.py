# authentication_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("login/", LoginView.as_view(), name="registration/login"),
    path("logout/", LogoutView.as_view(), name="registration/logout"),
    path("signup/", views.signup, name="signup"),
    path("visualization/", views.visualization_view, name="visualization_view"),
]
