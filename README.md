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

- open `http://localhost:5002` in preferred web browser (or whatever port number used for host)

_Note that if any files were edited, container must be stopped then restarted_

## Standup Reports

## Standup Report - 04 April 2025

Joel Kim @joel-d-kim

- did: trained model
- doing: implementing model to ml client folder
- blockers: none

Tim Xu @timxu23

- did: set up project structure
- doing: creating signup and login functionality
- blockers: none

Dibuk Seid @dibukseid

- did: created build.yaml file
- doing: preparing for ml client predictions
- blockers: none

Imran Ahmed @mxa5251

- did: merged tim's pull request
- doing: styling changes for front end
- blockers: none

## Standup Report - 05 April 2025

Joel Kim @joel-d-kim

- did: implemented model in ml client
- doing: creating preprocessing image function
- blockers: none

Tim Xu @timxu23

- did: set up docker environment
- doing: creating tests
- blockers: none

Dibuk Seid @dibukseid

- did: wireframed ui for translation predictions
- doing: preparing for ml client predictions
- blockers: none

Imran Ahmed @mxa5251

- did: made some styling changes to front end
- doing: researching ways to send data from web app to ml client
- blockers: none

## Standup Report - 06 April 2025

Joel Kim @joel-d-kim

- did: setting up preprocessing images for model
- doing: setting up model predictions
- blockers: none

Tim Xu @timxu23

- did: set up camera page and route
- doing: creating tests
- blockers: none

Dibuk Seid @dibukseid

- did: came up with color scheming
- doing: reviewing pull requests
- blockers: waiting for model to be able to predict signs

Imran Ahmed @mxa5251

- did: set up db for image frames
- doing: creating route to send image to db for image frames
- blockers: none

## Standup Report - 07 April 2025

Joel Kim @joel-d-kim

- did: finalized model prediction pipeline
- doing: validating predictions with real image data
- blockers: refining model accuracy for edge cases

Tim Xu @timxu23

- did: wrote initial test cases and configured Pipfiles
- doing: expanding test coverage for auth and camera routes
- blockers: waiting for consistent model outputs to validate tests

Dibuk Seid @dibukseid

- did: added UI placeholders for displaying model predictions
- doing: integrating model outputs into UI dynamically
- blockers: waiting for finalized prediction endpoints

Imran Ahmed @mxa5251

- did: completed camera route to push images to database
- doing: testing sending images to db with multiple inputs
- blockers: syncing with frontend to confirm image capture triggers

## Standup Report - 08 April 2025

Joel Kim @joel-d-kim

- did: tested predictions across multiple signs
- doing: tuning model parameters for consistency
- blockers: minor inconsistencies in live input predictions

Tim Xu @timxu23

- did: added unit tests for camera and DB route
- doing: refactoring test suite for modularity
- blockers: needing more stable image samples for test mocks

Dibuk Seid @dibukseid

- did: connected UI to receive and display live predictions
- doing: refining layout for real-time feedback
- blockers: latency in displaying prediction results

Imran Ahmed @mxa5251

- did: verified image storage in DB from camera stream
- doing: handling edge cases in route input validation
- blockers: occasionally dropped frames

## Standup Report - 09 April 2025

Joel Kim @joel-d-kim

- did: achieved stable predictions with >90% accuracy
- doing: documenting model usage for integration
- blockers: none

Tim Xu @timxu23

- did: completed comprehensive test coverage
- doing: writing documentation for test and Pipfile setup
- blockers: none

Dibuk Seid @dibukseid

- did: finalized UI elements for displaying predictions
- doing: polishing styling and user feedback flow
- blockers: none

Imran Ahmed @mxa5251

- did: ensured teh route to the db was working
- doing: writing usage instructions for camera route
- blockers: none
