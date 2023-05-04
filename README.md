<h1 align="center">Labos Exercize</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-2.3.2-lightgreen">
  <img src="https://img.shields.io/badge/Python-3.9-green">
  <img src="https://img.shields.io/badge/Nginx-1.24.0-darkgreen">
  <img src="https://img.shields.io/badge/Docker-v23.0.5-blue">
</p>

<p align="left">First of all, it was really fun to perform the task :), here is some information about my solution for the task</p>

## Prerequisites

- VM with any distribution Linux, and Docker installed from version 20.10 (mandatory for this solution!).

## Files
<p>The solution is divided into 2 parts and consists of several files</p>

### Flask
- date.html - the template of the flask app
- main.py - the flask app
- requirements.txt - list of the dependencies off the flask app
- Dockerfile-flask - the dockerfile to build the flask app

### Nginx
- Nginx-date.conf - the custom nginx configuration file with the route of the path /hello to the flask app
- Dockerfile-nginx - the dockerfile to build the app nginx

## Important notes
- Please build the images and run them with the following commands:
```
docker build -t date-flask -f Dockerfile-flask /path/to/Dockerfile/folder
docker run -d --name date-flask -p 8080:8080 date-flask:latest
docker build -t date-nginx -f Dockerfile-nginx /path/to/Dockerfile/folder
docker run -d --add-host=host.docker.internal:host-gateway -p 80:80 --name date-nginx date-nginx:latest
```
- Please remember to add '/' at the end of the path while you are checking the solution, for example:
```
curl http://localhost/hello/
```
