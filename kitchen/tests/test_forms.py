from django.test import TestCase

from kitchen.forms import CookCreationForm, CookUpdateForm


class TestForms(TestCase):
    def test_cook_creation_form_with_years_of_experience(self):
        form_data ={
            "username": "Test",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "FirstTest",
            "last_name": "SecondTest",
            "years_of_experience": 1,
        }
        form = CookCreationForm(data=form_data)
        #print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_update_form_with_email_and_years_of_experience(self):
        form_data ={
            "years_of_experience": 5,
            "email": "",
        }
        form = CookUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
