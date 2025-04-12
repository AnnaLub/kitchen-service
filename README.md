# kitchen-service
Kitchen Service is an application for effective management of the restaurant kitchen and will help the restaurant owner to improve communication and rules among chefs in the kitchen.
This is a management system where chefs will be able to create new dishes and their types, as well as indicate which chefs are responsible for preparing each dish.
<br>

## Data structure
![img_2.png](img_2.png)

<br>

## Functions
1.Dish Management: Create, update, and delete dishes.
2.Ingredient Management: Track and manage ingredients for each dish.
3.Dish Type Management: Categorize dishes by their type.
4.Search Functionality: Easily search for dishes and ingredients.
5.User Authentication: Secure login and registration for kitchen staff.
<br>

## Installation
Python3 must be already installed

### Clone the repository:
"git clone https://github.com/AnnaLub/kitchen-service"

### Create a virtual environment and activate it:
"python -m venv .venv
.venv\Scripts\activate (on Windows)
source .venv/bin/activate (on macOS)"

### Install the project dependencies:
"pip install -r requirements.txt"

### Create a database and migrate the models:
"python manage.py migrate"

### Create a superuser:
"python manage.py createsuperuser"

### Start the server:
"python manage.py runserver"

 Open your web browser and go to
http://127.0.0.1:8000.

<br 
### Home Page
<img src="static/img/illustrations/2025-04-11.png" alt="">

