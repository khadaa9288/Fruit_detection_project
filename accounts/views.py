from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# =========================================================
# REGISTER
# =========================================================

def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


# =========================================================
# LOGIN
# =========================================================

def user_login(request):

    if request.user.is_authenticated:

        if request.user.is_staff:
            return redirect("/admin/")

        return redirect("home")

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # ---------------------------------------------
            # ADMIN / SUPERUSER
            # ---------------------------------------------

            if user.is_staff:
                return redirect("/admin/")

            # ---------------------------------------------
            # NORMAL USER
            # ---------------------------------------------

            return redirect("home")

        error = "Invalid username or password."

    return render(
        request,
        "accounts/login.html",
        {"error": error}
    )


# =========================================================
# PROFILE + PREDICTION HISTORY
# =========================================================

@login_required(login_url="/login/")
def profile(request):

    predictions = request.user.fruit_predictions.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "accounts/profile.html",
        {
            "predictions": predictions
        }
    )