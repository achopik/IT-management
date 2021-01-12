#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then

    echo "Waiting for PostgreSQL"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate

# Config for Django dev server
python manage.py runserver 0.0.0.0:8000

# Config for gunicorn
#python manage.py collectstatic --noinput
#gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers=2


exec "$@"