# This is a Simple Django Project

## Follow Along the mentioned Steps:

___**Clone This Repository:**___ <br>

```
https://github.com/Shubhashish-Chakraborty/Amazon_Order_Sample.git
```

<hr>

**Create/Setup the Virtual Environment :** <br>

```
pip install uv
```

```
uv venv
```

<hr>

**Activate the Virtual Environment:** <br>

| System          | Command                     |
| --------------- | --------------------------- |
| macOS and Linux | `source .venv/bin/activate` |
| Windows      | `.venv\Scripts\activate`    |

<hr>

**Install Required Packages:** <br>

```

uv pip install -r requirements.txt

```

<hr>

**Move to the Project Directory:** <br>

`>>> cd .\CART_MAIN\`

<hr>

**Make Migrations:** <br>

```
python manage.py migrate
```

**Create Superuser:** <br>


```
python manage.py createsuperuser
```

> Give all the neccesary inputs

## RUN THE SERVER

``` python

# Default PORT : 8000
>>> python manage.py runserver

# If you want to give your selective PORT:
>>> python manage.py runserver 3000

```