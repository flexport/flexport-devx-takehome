FROM python:3.10.10-slim

WORKDIR /app

COPY ./src ./src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "--app", "src/rock_paper_scissors/app", "run"]
