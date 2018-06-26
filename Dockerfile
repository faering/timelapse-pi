# Import a Python 3 runtime image
FROM python:3

# Set working directory to "/app"
WORDIR /app

# Copy the current directory contents into container at "/app"
ADD . /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
	picamera

# Run app.py when container launches
CMD ["python", "app.py"]
