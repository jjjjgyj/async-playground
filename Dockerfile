# Use the python base image
FROM python:3.13

# Copy the script file into the Docker image
COPY /app/test_async.py /app/test_async.py

# Set the working directory
WORKDIR /app

# Run the script
CMD ["python", "test_async.py"]
