FROM python:3.10

WORKDIR /web-app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . .

CMD [ "pipenv", "run", "python3", "run.py" ]
