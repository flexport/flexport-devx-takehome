FROM python:3.10

WORKDIR /app

# COPY CODE TO /APP
COPY . .

# Install Dependencies
RUN pip install -r requirements.txt

ENV PYTHONPATH="./src"

# Entry point to run app
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run", "--host", "0.0.0.0"]