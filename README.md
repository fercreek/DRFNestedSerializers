# Nested Serializers

In the panel to add information, you will see **Lists are not currently supported in HTML input**,
that's it normal.

### Installation
1. Create your own environment (virtualenv, virtualenvwrapper, etc)
1. pip install -r requirements.txt
1. python manage.py makemigrations
1. python manage.py migrate
1. python manage.py runserver


Raw data
``` json
{
    "ingredients": [],
    "name": "",
    "description": "",
    "directions": ""
}
```

Adding existing ingredients, and recipe.
``` json
{
    "ingredients": [
      {"name":"pepper"},
      {"name":"salt"}
    ],
    "name": "Sandwich",
    "description": "Make me a Sandwich",
    "directions": "Sudo !!"
}
```

Adding exist ingredients and recipe
``` json
{
    "ingredients": [
      {"id": 1, "name":"pepper"},
      {"id": 2, "name":"salt"}
    ],
    "name": "Sandwich",
    "description": "Make me a Sandwich",
    "directions": "Sudo !!"
}
```
