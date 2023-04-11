FROM python:3.11
WORKDIR /app
COPY . /app
COPY requirements.txt ./
ENV PYTHONPATH "${PYTHON_PATH}:./src"
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run", "-h", "0.0.0.0"]
