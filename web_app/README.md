# Multi-Container Flask Application with Redis and NGINX

This project is a multi-container Docker application built to demonstrate how web services communicate with databases, persist data, and sit behind a reverse proxy in a real-world DevOps-style setup.

The system uses Flask for the web application, Redis for persistent storage, NGINX as a reverse proxy, and Docker Compose for orchestration.



## Architecture Overview

This application consists of three core services:

- Flask Web Application  
- Redis Database  
- NGINX Reverse Proxy  

Traffic flows from the client to NGINX.  
NGINX forwards requests to the Flask container.  
Flask stores and retrieves data from Redis using Docker’s internal network.



## Project Structure

    web_app/
    ├── flask/
    │   ├── app.py
    │   └── Dockerfile
    ├── nginx/
    │   └── nginx.conf
    ├── redis/
    │   └── Dockerfile
    ├── docker-compose.yml
    └── README.md



## Features

- Multi-container orchestration using Docker Compose  
- Internal container networking  
- Persistent Redis storage with Docker volumes  
- Reverse proxy routing using NGINX  
- Environment variable based configuration  
- Real-world service isolation and communication  



## Application Behaviour



### Flask Web Application

The Flask application exposes two routes.

1. `/`  
   Displays a simple welcome message.

2. `/count`  
   Increments and displays a visit count stored in Redis.

Each time `/count` is refreshed, Redis updates the value using:

    visits = redis_client.incr("visits")



### Redis Persistence

Redis runs in its own container and acts as a persistent key-value store for the visit counter.

It uses a Docker volume so the count:

- Does not reset if the container restarts  
- Persists across application shutdowns  



### Environment Variables

The Flask application does not hardcode infrastructure values.

Instead, it uses the following environment variables:

- REDIS_HOST  
- REDIS_PORT  
- REDIS_DB  

These variables are injected through `docker-compose.yml`, keeping the application portable and production-ready.



### NGINX Reverse Proxy

An NGINX container sits in front of the Flask application and:

- Listens externally on port 5002  
- Forwards incoming requests to the Flask container internally  
- Decouples client traffic from the application  

This mirrors how real production systems handle traffic routing.



## Docker Setup



### Flask Dockerfile

This Dockerfile builds a lightweight Python runtime for the Flask application.

    FROM python:3.8-slim

    WORKDIR /app

    COPY app.py .

    RUN pip install flask redis

    EXPOSE 5002

    CMD ["python", "app.py"]



### Redis Dockerfile

This Dockerfile uses the official Redis image.

    FROM redis



### Docker Compose Responsibilities

Docker Compose is used to:

- Orchestrate multiple services  
- Create an internal Docker network  
- Provide persistent storage with volumes  
- Route traffic using NGINX  
- Inject environment variables cleanly  



## How to Run the Project Locally

From the root directory of the project, run:

    docker compose up --build

Once running, access the application using:

- Welcome Page  
  http://localhost:5002/

- Visit Counter  
  http://localhost:5002/count

Each refresh on `/count` increments the Redis-backed counter.



## What This Project Demonstrates

- Multi-container application design  
- Internal Docker networking  
- Service isolation with controlled communication  
- Persistent state outside application memory  
- Reverse proxy traffic flow  
- Real-world Docker Compose orchestration  



## Future Improvements

- Add health checks for all services  
- Introduce logging and monitoring  
- Scale the Flask service horizontally  
- Deploy the application to a cloud environment  