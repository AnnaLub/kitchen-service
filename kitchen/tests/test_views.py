
from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from kitchen.models import DishType, Dish, Cook, Ingredient


DISH_LIST_URL = reverse("kitchen:dish-list")


class PublicTest(TestCase):
    def test_login_required_dish_list(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_home_page(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_cook_list(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="1234test"
        )
        self.client.force_login(self.user)

        number_of_dishes = 5
        dish_type = DishType.objects.create(name="test-type")

        for dish_id in range(number_of_dishes):
            Dish.objects.create(name=f"test-dish{dish_id}",
                                dish_type=dish_type,
                                price=10,
                                )

    def test_retrieve_dish_list(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes),
        )

    def test_dish_list_uses_correct_template(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_search_by_dish_name(self):
        dishes = Dish.objects.filter(name__icontains="test-dish0")
        response = self.client.get(DISH_LIST_URL + "?name=test-dish0")
        self.assertEqual(list(response.context["dish_list"]),
                         list(dishes))

    def test_pagination_is_five(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertTrue("is_paginated" in response.context)
        self.assertEqual(len(response.context["dish_list"]), 5)

    def test_switch_responsibility_for_dish(self):
        dish = Dish.objects.get(id=1)
        url = reverse("kitchen:switch-responsibility", args=[dish.id])
        self.client.post(url)
        self.assertEqual(len(dish.cooks.all()), 1)
        self.assertIn(self.user, dish.cooks.all())

        self.client.post(url)
        self.assertNotIn(self.user, dish.cooks.all())


class PrivateTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="1234test"
        )
        self.client.force_login(self.user)
        self.user = get_user_model().objects.create_user(username="test-2",
                                                         password="1111test")
        self.ingredient = Ingredient.objects.create(name="ingredient-test")
        self.dish_type = DishType.objects.create(name="type-test")
        self.dish = Dish.objects.create(name="test",
                                        dish_type=self.dish_type,
                                        price=10)

    def test_retrieve_home_pege(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["num_ingredients"],
                         Ingredient.objects.count())
        self.assertEqual(response.context["num_dish_types"],
                         DishType.objects.count())
        self.assertEqual(response.context["num_dishes"],
                         Dish.objects.count())
        self.assertEqual(response.context["num_cooks"],
                         Cook.objects.count())

    def test_retrieve_ingredient_list(self):
        response = self.client.get(reverse("kitchen:ingredient-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["ingredient_list"]),
                         list(Ingredient.objects.all()))

    def test_retrieve_cook_list(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]),
                         list(Cook.objects.all()))

    def test_retrieve_dysh_type_list(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_type_list"]),
                         list(DishType.objects.all()))

    def test_search_cook_by_username(self):
        search_field = "t"
        cooks = Cook.objects.filter(username__icontains=f"{search_field}")
        response = self.client.get(
            reverse("kitchen:cook-list") + f"?username={search_field}")
        self.assertEqual(list(response.context["cook_list"]),
                         list(cooks))

    def test_search_ingredient_by_name(self):
        ingredients = Ingredient.objects.filter(name__icontains="e")
        response = self.client.get(
            reverse("kitchen:ingredient-list") + "?name=e")
        self.assertEqual(list(response.context["ingredient_list"]),
                         list(ingredients))

    def test_search_dysh_type_by_name(self):
        search_field = "test"
        dish_types = DishType.objects.filter(name__icontains=f"{search_field}")
        response = self.client.get(
            reverse("kitchen:dish-type-list") + f"?name={search_field}")
        self.assertEqual(list(response.context["dish_type_list"]),
                         list(dish_types))
