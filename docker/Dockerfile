FROM python:3.8.5-buster

EXPOSE 8080

COPY ./Pipfile.lock /opt
COPY ./pybotweb /opt/pybotweb

WORKDIR /opt

RUN pip install pipenv \
 && pipenv sync

ENTRYPOINT ["pipenv", "run", "python", "/opt/pybotweb/pybotweb.py"]

