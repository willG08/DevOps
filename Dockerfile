# Use the latest official Ubuntu image as the base
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3, pip, and curl for dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    python3-venv \
    && apt-get clean

# Create a virtual environment
RUN python3 -m venv /venv

# Install the requests library inside the virtual environment
RUN /venv/bin/pip install requests

# Set the working directory to /app
WORKDIR /app

# Copy the main.py script from the root of the repository to the container's /app directory
COPY main.py /app/main.py

# Set the default command to run your script using the virtual environment's python
CMD ["/venv/bin/python", "main.py"]
