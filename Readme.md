# KPA Backend 


## Setup 

### ✅ prerequisites

#### With Docker 
- docker and docker compose 

#### Without Docker
- python 3.10+
- [poetry](https://python-poetry.org/docs/#installation)
- Make – to use the provided Makefile commands (Optional)
- Postgres


## 🛠️ setup instructions

### using docker (preferred)
#### 1. clone the repository
```bash
git clone https://github.com/pankajvishw50/kpa-backend.git
cd kpa-backend 
```

#### 2. configure all .env files
there are multiple `name.env-example` files in this repo.
copy them in `name.env` by removing `-example`.
set values

#### 3. build and start container 
```bash
make compose-up-build
```

#### 4. setup db 
enter backend container shell
```bash
make backend-bash
```

Now run this from inside container shell
```bash
make makemigrate
```

That's It. I Hope everything is working right.

## Without Docker
You can install this project without docker and even without make tool
but you would have to do little hard work. 

- First make sure Poetry is available on your system.
- If you don't have make tool then check make files for each command/rule used in this docs and replace by those.

#### 1. clone the repository
```bash
git clone https://github.com/pankajvishw50/kpa-backend.git
cd kpa-backend 
```

#### 2. configure all .env files
there are multiple `name.env-example` files in this repo.
copy them in `name.env` by removing `-example`.
set values

#### 3. Install dependency
```bash
poetry sync --all-groups
```

#### 4. setup db 
```bash
make makemigrate
```

#### 5. Run App
```bash
make runserver
```

## API documentation (OpenAPI)
This repository includes a full openapi.yaml file located at the root of the project. It defines the complete API schema using the OpenAPI 3.0 standard.

### How to view the API docs
You can explore the API interactively using Swagger Editor:

- Go to https://editor.swagger.io
- Click on File > Import File and select openapi.yaml file
OR copy and paste entire openapi.yaml file


You’ll see a full, interactive API reference with all endpoints, parameters, responses, and models.


## Tech Stack
- Django as backend framework
- Django Rest Framework
- Postgres as database
- Docker for containerization
- Poetry for python package management

## Things to Note

- By Default App runs on 0.0.0.0:7878 Port.
- Make sure these ports are availble. if not configure project accordingly.
    - 7878 (APP)
    - 5432 (DB)
- You can define you own settings related to django application inside
    local/local.settings.py, this file is not tracked by git.
    there is an template availabe you can copy that `/kpa/settings/templates/local.settings.py`

