FROM python:3.10 as build
ENV PYTHONUNBUFFERED 1
WORKDIR /code

# Upgrade pip
RUN pip install --upgrade pip

# Install system's dependencies
# RUN apt-get update -y
# RUN apt-get install gettext -y

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Adds our application code to the image
COPY . .
RUN python manage.py collectstatic

FROM nginx:stable-alpine
COPY --from=build /code/files/static /files/static
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8001
CMD [ "nginx", "-g", "daemon off;" ]
