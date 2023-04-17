FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHON_PATH}:./src"
EXPOSE 5000

CMD ["flask", "--app", "src/rock_paper_scissors/app", "run" , "-h", "0.0.0.0"]
