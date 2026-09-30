from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [

    path(
        "login/",
        views.user_login,
        name="login"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

]