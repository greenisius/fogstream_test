FROM python:3.6-stretch
MAINTAINER greenisius

RUN pip install Django 

COPY . .

EXPOSE 7777/tcp

CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]