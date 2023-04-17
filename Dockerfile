FROM python:3.9

WORKDIR ./

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#ENV FLASK_APP=/src/rock_paper_scissors/app.py
ENV PYTHONPATH="${PYTHON_PATH}:./src"
EXPOSE 5000

#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run" , "-h", "0.0.0.0"]
