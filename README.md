# кулинарная книга (django)

### Стек:
Python = 3.11
Django = 5.0.1
### Запуск проекта локально:
- Активировать poetry и установить зависимости проекта
```
poetry shell
``` 
```
poetry install
``` 
- Перейти в папку с manage.py и запустить миграции и локалсервер, также создать суперюзера для доступа к админке:
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
### Примеры URL с реализацией функций согласно тз:
- http://127.0.0.1:8000/api/recipes/add_product_to_recipe/?product_id=15&recipe_id=44&weight=234
- http://127.0.0.1:8000/api/recipes/cook_recipe/?recipe_id=44
- http://127.0.0.1:8000/api/recipes/show_recipes_without_product/?product_id=15