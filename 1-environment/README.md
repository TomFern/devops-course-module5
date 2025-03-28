# Module 6 - Deployment environments

**Goal**: Learn to create multiple environments using Docker

## Steps

1. Observe and discuss the following files, how does it manages environments?

- `docker-compose.yml`
- `Dockerfile`
- `app.py`

2. Start two environments with a single command: `docker compose up --build`
3. Visit localhost:4000 and localhost:4001, notice these are different environments, both handled by Docker simultanenously.
4. Stop the environments with `docker compose down`
