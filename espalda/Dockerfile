# Use an official Python runtime as a parent image
# We use a slim version for smaller image size
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir is used to prevent pip from caching packages, reducing image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
# This includes main.py, interfaz.py, etc.
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the uvicorn server when the container launches
# Listen on 0.0.0.0 to be accessible from outside the container
# Use the exec form for CMD to allow signals to be properly handled
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]