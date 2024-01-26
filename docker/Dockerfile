# Use the official image as a parent image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the file from your host to your current location
ADD .. /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
CMD ["python", "main.py"]