# Foro de trifulca

Basado en https://github.com/nitely/spirit-heroku

Ingresá desde https://foro.trifulca.com.ar/

## Ejecutar en modo desarrollo

Para ejecutar la aplicación de forma local, se pueden ejecutar
estos comandos:

```
pipenv install
createdb spirit     # para crear la base de datos postgres

pipenv run python manage.py migrate
pipenv run python manage.py createcachetable
pipenv run python manage.py collectstatic

pipenv run python manage.py runserver
```

Y para tener un usuario inicial, se puede ejecutar este
comando:

```
pipenv run python manage.py createsuperuser
```

## Deploy a producción

El foro está publicado bajo dokku, así que para hacer deploys
se tiene que agregar la dirección del git de dokku y realizar
un push así:

```
git remote add dokku dokku@trifulca.com.ar:foro
git push dokku master -f
```
