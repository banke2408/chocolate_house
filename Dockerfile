# Use the official Python image as the base
FROM python:3.9-slim

# Set environment variables to prevent Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Gunicorn will use
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "chocolate_house.wsgi:application", "--bind", "0.0.0.0:8000"]

