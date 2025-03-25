from django import forms

from kitchen.models import Dish, Ingredient


class IngredientForm(forms.ModelForm):
    dish = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget= forms.CheckboxSelectMultiple,
        required=False,)

    class Meta:
        model = Ingredient
        fields = '__all__'