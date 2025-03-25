
from django.urls import path

from .views import  (index,
                     DishTypeListView,
                     DishTypeCreateView,
                     DishTypeUpdateView,
                     DishTypeDeleteView,
                     DishListView,
                     CookListView,
                     IngredientListView)

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("ingredients", IngredientListView.as_view(), name="ingredients-list"),
]

app_name = "kitchen"