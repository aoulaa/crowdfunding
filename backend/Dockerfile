FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /code

# Install system's dependencies
# RUN apt-get update -y
# RUN apt-get install gettext -y

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Adds our application code to the image
COPY . .
EXPOSE 8000
