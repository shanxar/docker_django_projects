# Django Microservices with Docker Compose

A beginner-friendly microservices project built with **Python, Django REST Framework, and Docker**. It consists of two independent REST API services — Student API and Course API — running in separate Docker containers and communicating over a custom Docker bridge network.

## Overview

This project demonstrates how to containerize multiple Django applications and enable HTTP communication between services using Docker Compose.

- **Student Service (App1):** Provides student information and retrieves course details from the Course Service.
- **Course Service (App2):** Provides course information through a REST API.
- **Docker Compose:** Builds and runs both services together.
- **Custom Bridge Network:** Enables communication between containers using Docker service names.

## Architecture

```text
                 Client / Browser
                        |
             +----------+----------+
             |                     |
             v                     v
       localhost:8000        localhost:8001
             |                     |
      +--------------+      +--------------+
      |   App1       |      |   App2       |
      | Student API  |      | Course API   |
      | Django + DRF |      | Django + DRF |
      +--------------+      +--------------+
             |                     ^
             | HTTP request        |
             +---------------------+
               app2:8000/api/course/

          Docker Bridge Network
           student-course_network
```

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- Requests
- Docker
- Docker Compose
- Docker Bridge Networking
- REST APIs and HTTP/JSON

## Project Structure

```text
django_microservice/
├── app1/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/
│   └── api/
├── app2/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/
│   └── api/
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Prerequisites

Install the following before running the project:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Docker Compose, or Docker Engine with the Compose plugin.
- Git (optional, for cloning the repository).

Verify your installation:

```bash
docker --version
docker compose version
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the example GitHub URL with your repository URL.

### 2. Build and start the services

Run the following command from the project root, where `docker-compose.yml` is located:

```bash
docker compose up --build -d
```

This builds the Docker images and starts both containers in the background.

### 3. Check container status

```bash
docker compose ps
```

### 4. View application logs

```bash
docker compose logs -f
```

Press `Ctrl+C` to stop following the logs. The containers continue running.

## API Endpoints

| Service | Method | Endpoint | Purpose |
|---|---|---|---|
| Student API | GET | `http://localhost:8000/api/student/` | Returns student information and course details |
| Course API | GET | `http://localhost:8001/api/course/` | Returns course information |

### Test the Course API

```bash
curl http://localhost:8001/api/course/
```

Example response:

```json
{
  "course_id": 101,
  "course_name": "Docker with Django REST Framework",
  "duration": "2 weeks",
  "status": "available"
}
```

### Test the Student API

```bash
curl http://localhost:8000/api/student/
```

The Student API returns student information along with the course data retrieved from App2.

## How Inter-Service Communication Works

App1 sends an HTTP GET request to App2 using Python's `requests` library.

```python
requests.get(
    "http://app2:8000/api/course/",
    timeout=5
)
```

Here, `app2` is the Docker Compose service name. Docker's internal DNS resolves it to the App2 container on the shared network.

**Why not use `localhost:8001` inside App1?**

Inside a container, `localhost` refers to that same container. App1 must use App2's service name and internal container port to reach the other application.

## Docker Configuration

### Port Mapping

```yaml
ports:
  - "8000:8000"
```

The format is `HOST_PORT:CONTAINER_PORT`.

- App1: host port `8000` maps to container port `8000`.
- App2: host port `8001` maps to container port `8000`.

Both applications can listen on port `8000` inside their own containers.

### Custom Network

Both services are connected to the `student-course_network` bridge network. This allows the containers to communicate using service names without relying on host port mappings for internal requests.


## Docker Commands

| Command | Description |
|---|---|
| `docker compose up --build -d` | Build images and start services |
| `docker compose ps` | View service status |
| `docker compose logs -f app1` | Follow Student API logs |
| `docker compose logs -f app2` | Follow Course API logs |
| `docker compose restart` | Restart services |
| `docker compose down` | Stop and remove containers and the Compose network |
| `docker images` | List local Docker images |
| `docker network ls` | List Docker networks |

## Troubleshooting


**502 Bad Gateway**
Check App1's error response and inspect App2's logs. Verify that App1 uses `http://app2:8000/api/course/` and that App2 is running.

**Service not ready**

Docker Compose's `depends_on` controls startup order but does not guarantee that App2 is ready to serve requests. Retry after startup or add a health check and readiness handling.

## Learning Outcomes

- Containerizing separate Django applications with Dockerfiles.
- Defining multi-container applications with Docker Compose.
- Configuring and inspecting Docker bridge networks.
- Understanding container ports versus host ports.
- Implementing service-to-service REST API communication.
- Debugging container logs, networking, and API errors.

## Future Improvements

- Add automated API tests using pytest.
- Add health checks and more resilient inter-service requests.
- Integrate PostgreSQL for persistent data storage.
- Add CI/CD with GitHub Actions or Jenkins.
- Use a production WSGI server such as Gunicorn instead of Django's development server.



## Author

Gowrishankar

GitHub: https://github.com/shanxar
