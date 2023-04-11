FROM python
WORKDIR /app
COPY ./src ./src
COPY requirements.txt ./
ENV PYTHONPATH "${PYTHON_PATH}:./src"
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run", "-h", "0.0.0.0"]
