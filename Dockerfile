FROM python:2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY app/requirements_base.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements_base.txt

COPY app /usr/src/app
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN python manage.py makemigrations

EXPOSE 8000

CMD ["/docker-entrypoint.sh"]

