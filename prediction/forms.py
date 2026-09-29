from django import forms


class PredictionForm(forms.Form):

    # =====================================================
    # FRUIT IMAGE
    # =====================================================

    fruit_image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
                "accept": "image/*"
            }
        )
    )

    # =====================================================
    # FRUIT SIZE
    # =====================================================

    size = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter fruit size",
                "step": "0.01"
            }
        )
    )

    # =====================================================
    # FRUIT WEIGHT
    # =====================================================

    weight = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter weight in grams",
                "step": "0.01"
            }
        )
    )

    # =====================================================
    # FRUIT WIDTH
    # =====================================================

    width = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter fruit width",
                "step": "0.01"
            }
        )
    )

    # =====================================================
    # FRUIT HEIGHT
    # =====================================================

    height = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter fruit height",
                "step": "0.01"
            }
        )
    )

    # =====================================================
    # FRUIT COLOR
    # =====================================================

    color = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Example: Red"
            }
        )
    )

    # =====================================================
    # FRUIT TEXTURE
    # =====================================================

    texture = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Example: Smooth"
            }
        )
    )

    # =====================================================
    # SWEETNESS
    # =====================================================

    sweetness = forms.FloatField(
        min_value=0,
        max_value=20,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter sweetness",
                "step": "0.01"
            }
        )
    )

    # =====================================================
    # ACIDITY
    # =====================================================

    acidity = forms.FloatField(
        min_value=0,
        max_value=20,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter acidity",
                "step": "0.01"
            }
        )
    )

    # =====================================================
    # RIPENESS
    # =====================================================

    ripeness = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Example: Ripe"
            }
        )
    )