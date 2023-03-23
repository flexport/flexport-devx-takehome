FROM python:3.10.10-slim

WORKDIR /app

RUN apt update && apt upgrade
RUN apt install -y curl

COPY ./src ./src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "src/rock_paper_scissors/app", "run" , "-h", "0.0.0.0"]