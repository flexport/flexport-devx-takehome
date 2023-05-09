FROM python:3.10.2-slim-buster

# RUN apk add --no-cache python3-dev \
# && pip3 install --upgrade pip

COPY . /app

# Create app directory
WORKDIR /app


# Install app dependencies
#COPY requirements.txt ./

RUN pip install -U -r requirements.txt

# # Bundle app source
# COPY . .

EXPOSE 5000
CMD [ "flask", "--app","/app/src/rock_paper_scissors/app","run","-h", "0.0.0.0"]
