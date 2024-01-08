"# Hexashop" 
 ### Hexashop

Hexashop is a simple e-commerce web application built using the Django web framework and the PostgreSQL database. It allows users to browse products, add them to a shopping cart, and checkout.

### Getting Started

To get started, you will need to install the following dependencies:

* Python 3.6 or later
* Django 3.2 or later
* PostgreSQL 12 or later

Once you have installed these dependencies, you can clone the Hexashop repository from GitHub:

```
git clone https://github.com/Mashaun18/Hexashop.git
```

Next, you will need to create a virtual environment and install the project dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Once the dependencies are installed, you can migrate the database:

```
python manage.py migrate
```

Finally, you can start the development server:

```
python manage.py runserver
```

The development server will be available at http://localhost:8000.

### Code Structure

The Hexashop project is structured as follows:

* `hexashop/`
    * `__init__.py`
    * `settings.py`
    * `urls.py`
    * `wsgi.py`
* `accounts/`
    * `__init__.py`
    * `admin.py`
    * `apps.py`
    * `forms.py`
    * `models.py`
    * `tests.py`
    * `views.py`
* `cart/`
    * `__init__.py`
    * `admin.py`
    * `apps.py`
    * `forms.py`
    * `models.py`
    * `tests.py`
    * `views.py`
* `checkout/`
    * `__init__.py`
    * `admin.py`
    * `apps.py`
    * `forms.py`
    * `models.py`
    * `tests.py`
    * `views.py`
* `orders/`
    * `__init__.py`
    * `admin.py`
    * `apps.py`
