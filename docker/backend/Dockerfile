FROM python:3.8.16

#install nano text editor in docker container
RUN apt-get update -y && apt-get install nano -y

# set work directory
WORKDIR /app/blog/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
ADD ../../requirements.txt /app/blog/
RUN pip install -r requirements.txt

ADD ../../ /app/blog/

RUN chmod +x /app/blog/docker/backend/entry-point/server-entrypoint.sh
RUN chmod +x /app/blog/docker/backend/entry-point/worker-entrypoint.sh


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


