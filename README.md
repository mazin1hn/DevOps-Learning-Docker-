# Docker Project Repository



## Overview

This repository documents my hands-on implementation of Docker through one complete multi-container application project.

The focus is on understanding how containers communicate, how services are orchestrated using Docker Compose, how reverse proxies work, how state is persisted using volumes, and how Dockerfiles are structured using multi-stage builds.

All work is applied directly through the [Web App](./web_app) project inside this repository.



## Why Docker Matters in DevOps

Docker standardises how applications are built, shipped, and executed across environments. It removes inconsistencies between development, testing, and production by packaging applications together with their runtime, dependencies, and configuration.

In real DevOps workflows, Docker is used for:

- Containerising applications for CI and CD pipelines  
- Running microservices-based systems  
- Standardising development and production parity  
- Supporting cloud-native and platform engineering workflows  

Docker is not just a developer tool. It is an operational standard across modern infrastructure.



## Repository Structure

This repository contains a single full multi-container project.

    DOCKER/
    ├── web_app/
    │   ├── flask/
    │   │   ├── app.py
    │   │   └── Dockerfile
    │   ├── nginx/
    │   │   └── nginx.conf
    │   ├── redis/
    │   │   └── Dockerfile
    │   ├── venv/
    │   ├── docker-compose.yml
    │   └── README.md
    └── README.md



## Project Overview

The [./web_app](./web_app) directory contains a full multi-container application composed of:

- A Python Flask web application built using a multi-stage Dockerfile  
- A Redis database used as a persistent key-value store  
- An NGINX reverse proxy  
- Docker Compose for orchestration  
- Docker volumes for state persistence  

Each service runs inside its own container and communicates over internal Docker networking.



## Core Docker Concepts Applied

- Building custom images using Dockerfiles  
- Multi-stage Docker builds for smaller and cleaner images  
- Running containers as non-root users  
- Service orchestration using Docker Compose  
- Internal container networking and DNS resolution  
- Environment variable configuration  
- Reverse proxy routing using NGINX  
- Volume-based data persistence  
- Multi-container architecture design  
- Debugging container connectivity issues  



## Tools and Technologies

- Docker  
- Docker Compose  
- Python Flask  
- Redis  
- NGINX  



## How to Run the Project

From inside the [./web_app](./web_app) directory:

    docker compose up --build

Once all services are running, open your browser:

- Welcome page:
  http://localhost:5002/

- Visit counter:
  http://localhost:5002/count

Each refresh on `/count` increments the value stored in Redis.



## Documentation

The full technical breakdown of the project is located inside:

- [Web App Project README](./web_app/README.md)



## Resources

- https://docs.docker.com  
- https://docs.docker.com/compose  
- https://nginx.org/en/docs  
- https://redis.io/docs  
