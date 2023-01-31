# To run this project at your local machine follow the steps bellow:

## 1 - Clone this Repository in your cli:

```
$ git clone git@github.com:Mazuquiebe/file-reader-python.git

```

<br>

## 2 - Create a virtual environment:

```
$ python -m venv venv
```

<br>

## 3 - Activate the virtual environment

### if you use Linux:

```
$ source venv/bin/activate
```

### elif use Windows:

```
$ .\venv\Sceipts\activate
```

<br>

## 3 - Install the required dependencies.

### With your virtual environment activated run the command below:

```
$ pip install -r requirements.txt
```

<br>

## 4 - Allow access through the localhost.

### In settings.py from this project:

```
ALLOWED_HOSTS = [..., "localhost"]
```

<br>

## 5 - Create a database.

### Knowing that you have installed in you machine the postgresql:

```
$ CREATE DATABASE my_database;
```

### if it succeeds:

```
$ CREATE DATABASE my_database;
CREATE DATABASE
```

## 6 - Create a .env file at the root from this project.

### Add the database credentials:

```
POSTGRES_USER = your user here.
POSTGRES_PASSWORD = your access password here.
POSTGRES_DB = my_database

SECRET_KEY = define a secret key here.

DEBUG=True
```

## 7 - Run the project

```
$ python manage.py runserver
```
