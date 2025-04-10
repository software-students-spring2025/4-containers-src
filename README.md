![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)
!badge goes here for web-app testing
!badge goes here for machine-learning-client testing

# Team name: src
This application allows the user to practice American Sign Language, and records the signed letters in a MongoDB database.  

# Group Members
[Imran Ahmed](https://github.com/mxa5251)
[Joel Kim](https://github.com/joel-d-kim)
[Dibuk Seid](https://github.com/dibukseid)
[Tim Xu](https://github.com/timxu23)

# Steps to run software
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

- open `http://localhost:5002` in preferred web browser (or whatever port number used for host) 

_Note that if any files were edited, container must be stopped then restarted_