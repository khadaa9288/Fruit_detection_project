from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# =========================================================
# REGISTER
# =========================================================

def register(request):

    # If already logged in, go to home
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            # Automatically login after registration
            login(request, user)

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


# =========================================================
# LOGIN
# =========================================================

def user_login(request):

    # -----------------------------------------------------
    # Already logged in
    # -----------------------------------------------------

    if request.user.is_authenticated:

        # Staff / Superuser → Django Admin
        if request.user.is_staff:
            return redirect("/admin/")

        # Normal user → Home
        return redirect("home")

    error = None

    # -----------------------------------------------------
    # Login form submitted
    # -----------------------------------------------------

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        # Check username and password
        user = authenticate(
            request,
            username=username,
            password=password
        )

        # -------------------------------------------------
        # Valid login
        # -------------------------------------------------

        if user is not None:

            # Login the user
            login(request, user)

            # ---------------------------------------------
            # ADMIN / STAFF USER
            # ---------------------------------------------

            if user.is_staff:

                return redirect("/admin/")

            # ---------------------------------------------
            # NORMAL USER
            # ---------------------------------------------

            return redirect("home")

        # -------------------------------------------------
        # Invalid login
        # -------------------------------------------------

        error = "Invalid username or password."

    # -----------------------------------------------------
    # Display login page
    # -----------------------------------------------------

    return render(
        request,
        "accounts/login.html",
        {
            "error": error
        }
    )


# =========================================================
# LOGOUT
# =========================================================

def user_logout(request):

    logout(request)

    return redirect("home")


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
