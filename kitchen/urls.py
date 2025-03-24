
from django.urls import path

from .models import Ingredient
from .views import  index, DishTypeListView, DishListView, CookListView, IngredientListView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("ingredients", IngredientListView.as_view(), name="ingredients-list"),
]

app_name = "kitchen"