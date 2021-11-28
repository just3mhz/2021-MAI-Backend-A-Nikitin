up:
	docker-compose up -d

test: up
	docker-compose exec webapp python3 manage.py test

migrate: up
	docker-compose exec webapp python3 manage.py migrate

down:
	docker-compose down
