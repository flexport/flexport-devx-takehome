FROM python:3.10

WORKDIR /app

COPY requirements.txt .

COPY src .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "src/rock_paper_scissors/app",  "run"]