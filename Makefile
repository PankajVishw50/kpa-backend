
BASE_DOCKER_COMPOSE=./docker-compose.yml
DEV_DOCKER_COMPOSE=./docker-compose-dev.yml


poetry:
	poetry run python3 manage.py $(ARGS)

runserver:
	poetry run python3 manage.py runserver 0.0.0.0:7878

shell:
	$(MAKE) poetry ARGS="shell"

shell_plus:
	$(MAKE) poetry ARGS="shell_plus"

makemigations:
	$(MAKE) poetry ARGS="makemigrations"

migrate:
	$(MAKE) poetry ARGS="migrate"

makemigrate: makemigations migrate

# Docker related rules
compose-prefix:
	docker compose $(ARGS)

compose-dev-prefix:
	docker compose \
		-f $(BASE_DOCKER_COMPOSE) \
		-f $(DEV_DOCKER_COMPOSE) \
		$(ARGS)

compose-up:
	$(MAKE) compose-prefix ARGS="up -d"
	
compose-up-build:
	$(MAKE) compose-prefix ARGS="up --build -d"

compose-restart:
	$(MAKE) compose-prefix ARGS="restart"

compose-down:
	$(MAKE) compose-prefix ARGS="down" 

compose-dev-up:
	$(MAKE) compose-dev-prefix ARGS="up -d"
	
compose-dev-up-build:
	$(MAKE) compose-dev-prefix ARGS="up --build -d"

compose-dev-restart:
	$(MAKE) compose-dev-prefix ARGS="restart"

compose-dev-down:
	$(MAKE) compose-dev-prefix ARGS="down" 

%-bash:
	$(MAKE) compose-prefix ARGS="exec $* bash"

logs:
	$(MAKE) compose-prefix ARGS="logs -f $(ARGS)"

%-logs:
	$(MAKE) logs ARGS="$*"
