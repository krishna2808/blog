#!/bin/sh

until cd /app/blog-project/blog/
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput
gunicorn blog.wsgi:application --bind 0.0.0.0:8000



#python manage.py runserver 0.0.0.0:8000

