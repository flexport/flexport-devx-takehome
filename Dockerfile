FROM python:3.9-slim

WORKDIR /app

# COPY CODE TO /APP
COPY . .

# Install Dependencies
RUN pip install -r requirements.txt

# Entry point to run app
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run", "--host", "0.0.0.0"]