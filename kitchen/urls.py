
from django.urls import path

from .views import  (index,
                     DishTypeListView,
                     DishTypeCreateView,
                     DishTypeUpdateView,
                     DishTypeDeleteView,
                     DishListView,
                     CookListView,
                     CookDetailView,
                     CookCreateView,
                     IngredientListView,
                     IngredientCreateView,
                     IngredientUpdateView,
                     IngredientDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/detail", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
]

app_name = "kitchen"