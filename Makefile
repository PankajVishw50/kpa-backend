
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

compose-up:
	$(MAKE) compose-prefix ARGS="up -d"
	
compose-up-build:
	$(MAKE) compose-prefix ARGS="up --build -d"

compose-restart:
	$(MAKE) compose-prefix ARGS="restart"

compose-down:
	$(MAKE) compose-prefix ARGS="down" 

%-bash:
	$(MAKE) compose-prefix ARGS="exec $* bash"

logs:
	$(MAKE) compose-prefix ARGS="logs -f $(ARGS)"

%-logs:
	$(MAKE) logs ARGS="$*"
