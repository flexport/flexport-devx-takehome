# Specify the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Expose the port that the application runs on
EXPOSE 5000

# Set the command to run the application
CMD ["flask", "--app", "src/rock_paper_scissors/app", "run"]