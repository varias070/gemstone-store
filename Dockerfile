FROM python:3.10

WORKDIR app
COPY ./sources ./
RUN pip install -r requirements.txt
# RUN python3 manage.py makemigrations | python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000