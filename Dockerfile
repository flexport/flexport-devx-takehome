FROM python:3.10

# Create a non-root user and group for better security
RUN groupadd -r app_group && useradd -r -g app_group app_user

WORKDIR /app

RUN chown app_user:app_group /app

USER app_user:app_group

COPY requirements.txt .

COPY src/ /app/src

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "src/rock_paper_scissors/app",  "run"]
