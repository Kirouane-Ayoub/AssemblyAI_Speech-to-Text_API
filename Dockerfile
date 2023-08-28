# Use the official Python base image
FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the application code into the container
COPY ./app  ./app

# Run the command to start the application
CMD ["python" , "./app/api.py"]

