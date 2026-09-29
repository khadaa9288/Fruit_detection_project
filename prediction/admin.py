from django.contrib import admin
from .models import FruitPrediction


@admin.register(FruitPrediction)
class FruitPredictionAdmin(admin.ModelAdmin):

    list_display = (
        "predicted_fruit",
        "confidence",
        "weight",
        "height",
        "width",
        "created_at",
    )

    list_filter = (
        "predicted_fruit",
        "created_at",
    )

    search_fields = (
        "predicted_fruit",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )