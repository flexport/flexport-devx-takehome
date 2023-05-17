# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

# COPY ./app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "src/rock_paper_scissors/app",  "run", "--host=0.0.0.0"]
