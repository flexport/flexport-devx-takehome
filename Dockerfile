# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run"]
