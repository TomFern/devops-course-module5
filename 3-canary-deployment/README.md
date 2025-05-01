# Module 6 - Deployment environments

**Goal**: Learn to perform canary deployments with Docker Compose

## Steps

1. Observe and discuss the following files, how does it manages environments? What's the purpose of nginx?

- `docker-compose.canary.yml`
- `Dockerfile`
- `app.py`
- `nginx.conf`

2. Start the stable and canary environments with the following command: `docker compose -f docker-compose.canary.yml up`
3. Navigate to localhost:8080, refresh the page several times. On average 10% of the times you should see the canary environment
7. Stop both environments using `CTRL+c`
