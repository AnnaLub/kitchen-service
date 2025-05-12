# Kitchen-service
Kitchen Service is an application for effective management of the restaurant kitchen and will help the restaurant owner to improve communication and rules among chefs in the kitchen.
This is a management system where chefs will be able to create new dishes and their types, as well as indicate which chefs are responsible for preparing each dish.
<br>

## Check it out!
https://restaurant-kitchen-service-qftx.onrender.com
* Login: test.admin
* Password: 1234
<br/>

## Data structure

![img_2.png](https://github.com/AnnaLub/kitchen-service/blob/develop/static/img/img_2.png)

<br/>

## Functions
1. Authentication functionality for Cook/Use.
2. Cook management: create, update and delete.
3. Ingredient management: create, update, delete.
4. Dish management: create, update and delete. Manage ingredients for each dish.
5. Dish Type Management: Categorize dishes by their type.
6. Search Functionality: Easily search for dishes and ingredients.

<br/>

## Installation
Python3 must be already installed

### 1.Clone the repository:
``` git clone https://github.com/AnnaLub/kitchen-service ```

### 2.Create a virtual environment and activate it:
``` python -m venv .venv```
```.venv\Scripts\activate (on Windows)```
```source .venv/bin/activate (on macOS) ```

### 3.Install the project dependencies:
``` pip install -r requirements.txt```

### 4.Create a database and migrate the models:
```  python manage.py migrate ```

### 5.Create a superuser:
``` python manage.py createsuperuser ```

### 6.Start the server:
```  python manage.py runserver```

 Open your web browser and go to
http://127.0.0.1:8000.

<br>

### Home Page
![2025-04-11.png](https://github.com/AnnaLub/kitchen-service/blob/develop/static/img/illustrations/2025-04-11.png)

