# Use the python base image
FROM python:3.13

# Copy the script file into the Docker image
COPY /app/test.py /app/test.py

# Set the working directory
WORKDIR /app

# Run the script
CMD ["python", "test.py"]
