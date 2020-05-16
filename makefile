.PHONY = tests	docker	docker-compose

tests:
	poetry run python -m pytest --cov=src.app -v unit-tests/app-tests.py
	poetry run python -m pytest --cov=src.users -v unit-tests/users-tests.py
	poetry run python -m pytest --cov=src.data_handler -v unit-tests/data_handler-tests.py

docker:
	docker build . -t mytestapiimg
	docker run --name mytestcontainer -p 80:8000 mytestapiimg

docker-delete:
	docker stop mytestcontainer
	docker rm mytestcontainer
	docker rmi mytestapiimg
