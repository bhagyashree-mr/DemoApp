# # Use the official Python 3.7 image as the base image
# # FROM python:3.7

#  # Set the working directory inside the container
# # WORKDIR /opt/simple-webapp-flask-master

#  # Copy the app.py file into the container's working directory
# # COPY app.py .

#  # Install Flask and other dependencies
# # RUN pip install flask

#  # Expose port 5000 for the Flask application
# # EXPOSE 5000

#  # Set the environment variable for Flask
# # ENV FLASK_APP=app.py

# # Start the Flask application when the container runs
# # CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# # Use an official Python runtime as a base image
# FROM python:3.8-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements.txt file into the container at /app
# COPY requirements.txt /app/

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Expose port 8080 for the application
# EXPOSE 5000

# # Define environment variable
# ENV FLASK_APP=app.py

# # Run the application
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 3000
CMD python ./app.py
