FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create virtual environment and install dependencies
RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt

# Populate the database
RUN venv/bin/python -m sql_app.populate_db

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World
ENV PORT 8000

# Run app.py when the container launches
CMD ["sh", "-c", "venv/bin/uvicorn main:app --host 0.0.0.0 --port ${PORT}"]

