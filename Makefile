install:
	poetry install

check:
	poetry check

start:
	poetry run gunicorn R4C.wsgi --reload

migration:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

lint:
	poetry run ruff .

test:
	poetry run python manage.py test

req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

env:
	mv .env.template .env
