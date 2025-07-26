
runserver:
	poetry run python3 manage.py runserver 0.0.0.0:7878

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
