# Module 6 - Deployment environments

**Goal**: Learn to perform blue-green deployments with Docker Compose

## Steps

1. Observe and discuss the following files, how does it manages environments?

- `docker-compose.blue-green.yml`
- `Dockerfile`
- `app.py`

2. Start the blue environment with the following command: `docker compose -f docker-compose.blue-green.yml up blue`
3. Navigate to localhost:4000, you are in the blue environment
4. Stop the blue environment using `CTRL+c`
5. Start the green environment with the following command: `docker compose -f docker-compose.blue-green.yml up green`
6. Navigate to localhost:4000, you are in the green environment
7. Stop the blue environment using `CTRL+c`
