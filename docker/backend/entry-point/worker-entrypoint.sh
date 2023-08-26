#!/bin/sh

until cd /app/blog
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A blog worker --loglevel=info --concurrency 1 -E
