#FROM scratch
FROM debian:bullseye-slim

WORKDIR /rps_app

COPY ./src ./src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /rps_app

EXPOSE 5000

CMD [ "flask", "--app" , "src/rock_paper_scissors/app", "run"]

HEALTHCHECK CMD curl --silent --fail --max-time 3 --connect-timeout 10 --max-time 10 \
                --connect-timeout 30 http://127.0.0.1:5000/health || exit 1

HEALTHCHECK CMD curl --silent --fail --max-time 3 --connect-timeout 10 --max-time 10 \
                --connect-timeout 30 -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/rps \
                -d '{"move": "Rock"}'  || exit 1
