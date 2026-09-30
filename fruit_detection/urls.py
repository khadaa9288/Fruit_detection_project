from django.contrib import admin
from django.urls import path

from prediction import views
from accounts import views as account_views

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # =====================================================
    # ADMIN
    # =====================================================

    path(
        "admin/",
        admin.site.urls
    ),


    # =====================================================
    # HOME
    # =====================================================

    path(
        "",
        views.home,
        name="home"
    ),


    # =====================================================
    # LOGIN
    # =====================================================

    path(
        "login/",
        account_views.user_login,
        name="login"
    ),


    # =====================================================
    # REGISTER
    # =====================================================

    path(
        "register/",
        account_views.register,
        name="register"
    ),


    # =====================================================
    # LOGOUT
    # =====================================================

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),


    # =====================================================
    # USER PROFILE / HISTORY
    # =====================================================

    path(
        "profile/",
        account_views.profile,
        name="profile"
    ),


    # =====================================================
    # PREDICTION
    # =====================================================

    path(
        "predict/",
        views.predict,
        name="predict"
    ),

]


# =========================================================
# MEDIA FILES
# =========================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )