FROM python:3.14-slim

EXPOSE 8080

COPY ./Pipfile.lock /opt
COPY ./pybotweb /opt/pybotweb

WORKDIR /opt

RUN pip install pipenv \
 && pipenv sync

WORKDIR /opt/pybotweb

ENTRYPOINT ["pipenv", "run", "python", "pybotweb.py"]

