# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY ./app
RUN pip3 install -r requirements.txt


CMD ["flask", "--app", "src/rock_paper_scissors/app",  "run", "--host=0.0.0.0"]
