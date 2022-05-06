# Introduction

This is a simple task management application. It provides basic functionality for company employee management like add/remove employee and task assignment for each employee.

### Technologies used in project:
* Django and Django-Rest-Framework
  
* Bootstrap 4.6 and jQuery
  
* Celery and RabbitMQ

* Swagger


### Prerequisites:
- Installed [Docker for Windows](https://docs.docker.com/docker-for-windows/install/) or [Linux](https://runnable.com/docker/install-docker-on-linux) 
- Installed [docker-compose](https://docs.docker.com/compose/install/) tool
- Cloned project repository


### Step by step guide: 
1. Open the command promt or terminal in the root directory with the `docker-compose` file.
2. Run `docker-compose up --build` command.
3. Open http://localhost:8000 in your browser.
4. When you finished working with the application press **CTRL+C** in your command prompt to terminate the process


### File upload

You can create quickly list of new employees by uploading a csv file with employee data. The file must have specific format as shown below, each column separated by comma ",":

| name | surname | position | month_salary |
| --- | --- | --- | --- |
| string up to 100 characters | string up to 100 characters | string up to 200 characters | decimal number with 8 digits, including 2 digit delimiter |