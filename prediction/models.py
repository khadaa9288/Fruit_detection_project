from django.db import models


class FruitPrediction(models.Model):

    # =====================================================
    # UPLOADED IMAGE
    # =====================================================

    image = models.ImageField(
        upload_to="fruit_predictions/"
    )

    # =====================================================
    # FRUIT FEATURES
    # =====================================================

    size = models.FloatField()

    weight = models.FloatField()

    width = models.FloatField()

    height = models.FloatField()

    color = models.CharField(
        max_length=50
    )

    texture = models.CharField(
        max_length=50
    )

    sweetness = models.FloatField()

    acidity = models.FloatField()

    ripeness = models.CharField(
        max_length=50
    )

    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    predicted_fruit = models.CharField(
        max_length=100
    )

    confidence = models.FloatField(
        default=0.0
    )

    # =====================================================
    # DATE / TIME
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self):

        return (
            f"{self.predicted_fruit} - "
            f"{self.created_at.strftime('%d-%m-%Y %H:%M')}"
        )