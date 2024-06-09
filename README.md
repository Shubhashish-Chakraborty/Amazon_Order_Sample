# This is a Simple Django Project

## Follow Along the mentioned Steps:

___**Clone This Repository:**___ <br>

`https://github.com/Shubhashish-Chakraborty/Amazon_Order_Sample.git`

<hr>

**Create/Setup the Virtual Environment :** <br>

`>>> pip install uv` <br>
`>>> uv venv`

<hr>

**Activate the Virtual Environment:** <br>

| System          | Command                     |
| --------------- | --------------------------- |
| On macOS and Linux | `source .venv/bin/activate` |
| On Windows      | `.venv\Scripts\activate`    |

<hr>

**Install Django and other Packages:** <br>

`>>> uv pip install django` <br>
`>>> uv pip install Pillow`

<hr>

**Move to the Project Directory:** <br>

`>>> cd .\CART_MAIN\`

<hr>

**Make Migrations:** <br>

`>>> python manage.py migrate`

**Create Superuser:** <br>

> Give all the neccesary inputs <br>
`>>> python manage.py createsuperuser`

## RUN THE SERVER

``` python

# Default PORT : 8000
>>> python manage.py runserver

# If you want to give your selective PORT:
>>> python manage.py runserver 3000

```