.PHONY: help start migrate loaddata

.DEFAULT: help
help:
	@echo "make start"
	@echo "       starts the db then starts identity and downstream apps"
	@echo "make migrate"
	@echo "       run manage.py migrate in the container against the db"
	@echo "make loaddata"
	@echo "       seed data for the app loads a few users and accounts"

start:
	docker-compose up -d identity_db
	docker-compose up -d identity downstream downstreamhtml

migrate:
	docker exec -it identity_identity_1 python manage.py migrate

loadata:
	docker exec -it identity_identity_1 python manage.py loaddata

