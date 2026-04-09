# Todo API — Docker Practice Project

A FastAPI + PostgreSQL + Alembic project for learning Docker.

## Project Structure

```
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── config.py        # App configuration (reads .env)
│   ├── database.py      # DB connection & session
│   ├── models.py        # SQLAlchemy models (DB tables)
│   ├── schemas.py       # Pydantic schemas (request/response)
│   └── routers/
│       └── todos.py     # Todo API routes
├── migrations/
│   ├── env.py           # Alembic config
│   ├── script.py.mako   # Migration template
│   └── versions/
│       └── 0001_create_todos_table.py
├── .env                 # Environment variables
├── .dockerignore
├── alembic.ini          # Alembic settings
├── docker-compose.yml   # Run app + db together
├── Dockerfile           # Build app image
└── requirements.txt     # Python dependencies
```

## Run with Docker

```bash
# Start everything
docker compose up --build

# Run in background
docker compose up --build -d

# Stop everything
docker compose down

# Stop and delete volumes (wipes database)
docker compose down -v
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /todos | List all todos |
| POST | /todos | Create a todo |
| GET | /todos/{id} | Get one todo |
| PATCH | /todos/{id} | Update a todo |
| DELETE | /todos/{id} | Delete a todo |
| GET | /health | Health check |
| GET | /docs | Swagger UI |

## Migrations

```bash
# Apply migrations
docker compose exec app alembic upgrade head

# Create a new migration
docker compose exec app alembic revision --autogenerate -m "your message"

# Rollback one step
docker compose exec app alembic downgrade -1

# Check current migration
docker compose exec app alembic current
```
