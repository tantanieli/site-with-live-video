FROM frolvlad/alpine-python3
RUN pip install django
RUN mkdir /mysite/
COPY mysite/ /mysite
ENTRYPOINT python /mysite/manage.py runserver 0:8000 
