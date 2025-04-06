FROM python:3.12

WORKDIR /web-app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "run.py"]