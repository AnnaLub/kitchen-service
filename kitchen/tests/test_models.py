from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


# Create your tests here.
class ModelsTest(TestCase):
    def test_create_cook_with_years_of_experience(self):
        username = "TestUser"
        password = "<PASSWORD>"
        years_of_experience = 20

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.password, password)

    def test_cook_str(self):
        username = "TestUser"
        password = "<PASSWORD>"
        first_name = "TestFirst"
        last_name = "TestLast"
        cook = get_user_model().objects.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        self.assertEqual(str(cook),
                         f"{cook.username}"
                         f" ({cook.first_name} {cook.last_name})")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test-type")
        dish = Dish.objects.create(name="test",
                                   dish_type=dish_type,
                                   price=10,
                                   )
        self.assertEqual(str(dish), dish.name)
