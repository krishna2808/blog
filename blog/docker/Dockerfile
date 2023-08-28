FROM python:3.8.16

#install nano text editor in docker container
RUN apt-get update -y && apt-get install nano -y && apt-get install nginx -y &&  apt-get install -y gunicorn systemd && apt-get install net-tools

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Create directory and sub-directory for project

RUN mkdir -p /app/blog-project/ 
# Add blog-project to  container.
ADD ../../ /app/blog-project/

# Create virtual environment and activate venv
# this venv active only on shell of session. it is not acitve all time. 
#RUN python -m venv /app/blog-project/venv
#RUN python -m venv /app/blog-project/venv && source /app/blog-project/venv/bin/activate


# set work directory
WORKDIR /app/blog-project/blog/


# install dependencies
RUN pip install --upgrade pip && pip install virtualenv
# Create a virtual environment
RUN virtualenv /app/blog-project/venv

# Set the Python interpreter to the venv's interpreter
ENV PATH="/app/blog-project/venv/bin:$PATH"

#ADD requirements.txt /app/blog/
RUN pip install -r requirements.txt 


# Create service for gunicorn server. it is possible to start server without create service but we will start, restart and stop gunicorn server using system service. 
RUN cp /app/blog-project/blog/docker/gunicorn/gunicorn.service /etc/systemd/ && cp /app/blog-project/blog/docker/gunicorn/gunicorn.socket /etc/systemd/   
#ADD /app/blog-project/blog/docker/gunicorn/gunicorn.socket /etc/systemd/system/
#RUN systemctl start gunicorn.socket && systemctl enable gunicorn.socket

RUN chmod +x /app/blog-project/blog/docker/backend/entry-point/server-entrypoint.sh
RUN chmod +x /app/blog-project/blog/docker/backend/entry-point/worker-entrypoint.sh


EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


