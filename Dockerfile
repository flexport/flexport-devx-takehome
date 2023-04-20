FROM python:3.9-slim

RUN apt-get -y update; apt-get -y install curl

RUN useradd --create-home appuser
USER appuser

WORKDIR /app

# COPY CODE TO /APP
COPY . .

# Install Dependencies
RUN pip install -r requirements.txt

ENV PYTHONPATH="./src"

# Entry point to run app
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run", "--host", "0.0.0.0"]