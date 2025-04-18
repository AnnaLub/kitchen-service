
from django.urls import path

from .views import (Index,
                    DishTypeListView,
                    DishTypeCreateView,
                    DishTypeUpdateView,
                    DishTypeDeleteView,
                    DishListView,
                    DishCreateView,
                    DishUpdateView,
                    DishDeleteView,
                    DishDetailView,
                    CookListView,
                    CookDetailView,
                    CookCreateView,
                    CookDeleteView,
                    CookUpdateView,
                    IngredientListView,
                    IngredientCreateView,
                    IngredientUpdateView,
                    IngredientDeleteView,
                    SwitchResponsibility,
                    )

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(),
         name="dish-type-create"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(),
         name="dish-type-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(),
         name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/crete/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(),
         name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(),
         name="dish-delete"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(),
         name="cook-delete"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(),
         name="cook-update"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(),
         name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(),
         name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(),
         name="ingredient-delete"),
    path("cooks/<int:pk>/switch_responsibility/",
         SwitchResponsibility.as_view(),
         name="switch-responsibility"),
]

app_name = "kitchen"
