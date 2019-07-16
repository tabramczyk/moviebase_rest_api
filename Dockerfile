FROM python:3.7
MAINTAINER Tomasz Abramczyk
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input;python manage.py makemigrations;python manage.py migrate;
CMD exec gunicorn moviebase.wsgi:application --bind 0.0.0.0:$PORT --workers 3