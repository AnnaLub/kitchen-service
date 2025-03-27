from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Dish, Ingredient, Cook


class IngredientForm(forms.ModelForm):
    dish = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget= forms.CheckboxSelectMultiple,
        required=False,)

    class Meta:
        model = Ingredient
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = (UserCreationForm.Meta.fields +
                  ("first_name", "last_name", "years_of_experience"))

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        return validate_year_of_experience(years_of_experience)


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_of_experience", "email",)

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        return validate_year_of_experience(years_of_experience)


def validate_year_of_experience(value: int):
    if value < 0:
        raise forms.ValidationError("year of experience must be positive")
    elif value > 30:
        raise forms.ValidationError("year of experience must be less than 30")
    return value