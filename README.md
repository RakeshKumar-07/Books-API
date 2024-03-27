# Books-API

Made using:-
  - Django RestFramework
  - Python

## How to Start

Run the following commands:-
```
cd <project_folder>
pip install django
pip install djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- login with superuser credentials at url http://127.0.0.1:8000/admin/
- got to http://127.0.0.1:8000/api/books to use app

## API Endpoints
- GET (http://127.0.0.1:8000/api/books)
- POST (http://127.0.0.1:8000/api/books)
- GET (http://127.0.0.1:8000/api/books/:isbn)
- PUT (http://127.0.0.1:8000/api/books/:isbn)
- DELETE (http://127.0.0.1:8000/api/books/:isbn)
