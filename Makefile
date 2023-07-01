.PHONY: run
run:
	docker-compose -f docker-compose.local.yml up --build

.PHONY: flake8
flake8:
	poetry run flake8 ./src --exclude config