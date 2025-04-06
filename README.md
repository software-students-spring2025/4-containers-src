![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

## Steps to run software

Required software:

- install and run [docker desktop](https://www.docker.com/get-started)
- create a [dockerhub](https://hub.docker.com/signup) account

Use Docker Compose to boot up both the mongodb database and the flask app using one command:

- Navigate to app directory which contains `Dockerfile`
- open Docker
- `docker compose up --build` ... add -d to run in detached/background mode.
- Ctrl + C then `docker compose down` when done to stop containers

If port number already use, select different port for `flask-app` or `mongodb` by changing their values in `docker-compose.yml`

View the app in browser:

- open `http://localhost:5001` in preferred web browser (or whatever port number used for host) 

_Note that if any files were edited, container must be stopped then restarted_