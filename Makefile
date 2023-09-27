install:
	poetry install

check:
	poetry check

start:
	poetry run gunicorn R4C.wsgi

shell:
	poetry run python manage.py shell

lint:
	poetry run ruff .

req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

env:
	mv .env.template .env
