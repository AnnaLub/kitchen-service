from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import IngredientForm
from .models import DishType, Dish, Cook, Ingredient

# Create your views here.
@login_required
def index(request:HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_ingredients": num_ingredients,
        "num_visits": num_visits,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen/cook_list.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5
    template_name = "kitchen/ingredient_list.html"
    queryset = Ingredient.objects.all().prefetch_related("dish")


class IngredientCreteView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    template_name = "kitchen/ingredient_confirm_delete.html"
    success_url = reverse_lazy("kitchen:ingredient-list")
