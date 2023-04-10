# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY ./src ./src
RUN apt-get update
RUN apt-get install -y curl
COPY requirements.txt ./
ENV PYTHONPATH "${PYTHON_PATH}:./src"
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run"]
