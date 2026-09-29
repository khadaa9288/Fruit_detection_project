import os
import joblib
import pandas as pd

from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import PredictionForm
from .models import FruitPrediction


# =========================================================
# MODEL PATH
# =========================================================

MODEL_PATH = os.path.join(

    settings.BASE_DIR,

    "prediction",

    "fruit_detection_model.pkl"

)


# =========================================================
# LOAD MODEL
# =========================================================

model = None


if os.path.exists(MODEL_PATH):

    model = joblib.load(
        MODEL_PATH
    )


# =========================================================
# HOME PAGE
# =========================================================

def home(request):

    return render(

        request,

        "prediction/home.html"

    )


# =========================================================
# PREDICTION PAGE
# =========================================================

def predict(request):

    prediction = None

    confidence = None

    image_url = None

    error = None


    # =====================================================
    # POST REQUEST
    # =====================================================

    if request.method == "POST":

        form = PredictionForm(

            request.POST,

            request.FILES

        )


        # =================================================
        # VALIDATE FORM
        # =================================================

        if form.is_valid():

            # ---------------------------------------------
            # CHECK MODEL
            # ---------------------------------------------

            if model is None:

                error = (
                    "ML model not found. "
                    "Please run train_model.py first."
                )


            else:

                # -----------------------------------------
                # FORM DATA
                # -----------------------------------------

                data = form.cleaned_data


                # -----------------------------------------
                # UPLOAD IMAGE
                # -----------------------------------------

                uploaded_image = request.FILES.get(
                    "fruit_image"
                )


                image_file = None


                if uploaded_image:

                    fs = FileSystemStorage(

                        location=settings.MEDIA_ROOT,

                        base_url=settings.MEDIA_URL

                    )


                    filename = fs.save(

                        uploaded_image.name,

                        uploaded_image

                    )


                    image_file = filename


                    image_url = fs.url(
                        filename
                    )


                # -----------------------------------------
                # PREPARE MODEL INPUT
                # -----------------------------------------

                input_data = pd.DataFrame(

                    [

                        {

                            "Fruit_Size":
                                data["size"],

                            "Fruit_Weight":
                                data["weight"],

                            "Fruit_Width":
                                data["width"],

                            "Fruit_Height":
                                data["height"],

                            "Fruit_Color":
                                data["color"],

                            "Fruit_Texture":
                                data["texture"],

                            "Sweetness":
                                data["sweetness"],

                            "Acidity":
                                data["acidity"],

                            "Ripeness":
                                data["ripeness"]

                        }

                    ]

                )


                # -----------------------------------------
                # PREDICT
                # -----------------------------------------

                prediction_result = model.predict(

                    input_data

                )


                prediction = str(

                    prediction_result[0]

                )


                # -----------------------------------------
                # CONFIDENCE
                # -----------------------------------------

                if hasattr(

                    model,

                    "predict_proba"

                ):

                    probabilities = (

                        model.predict_proba(

                            input_data

                        )

                    )


                    confidence = round(

                        float(

                            probabilities.max()

                        ) * 100,

                        2

                    )


                # -----------------------------------------
                # SAVE DATABASE RECORD
                # -----------------------------------------

                prediction_record = FruitPrediction(

                    size=data["size"],

                    weight=data["weight"],

                    width=data["width"],

                    height=data["height"],

                    color=data["color"],

                    texture=data["texture"],

                    sweetness=data["sweetness"],

                    acidity=data["acidity"],

                    ripeness=data["ripeness"],

                    predicted_fruit=prediction,

                    confidence=confidence or 0.0

                )


                # -----------------------------------------
                # SAVE IMAGE
                # -----------------------------------------

                if image_file:

                    prediction_record.image = image_file


                # -----------------------------------------
                # SAVE RECORD
                # -----------------------------------------

                prediction_record.save()


    # =====================================================
    # GET REQUEST
    # =====================================================

    else:

        form = PredictionForm()


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "form": form,

        "prediction": prediction,

        "confidence": confidence,

        "image_url": image_url,

        "error": error

    }


    # =====================================================
    # RENDER
    # =====================================================

    return render(

        request,

        "prediction/predict.html",

        context

    )