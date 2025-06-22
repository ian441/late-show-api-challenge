# Late Show API

A Flask-based REST API for managing a database of late show guests, built with SQLAlchemy and Alembic for migrations.

## Features

- RESTful API endpoints for managing resources
- Database migrations with Alembic via Flask-Migrate
- Seed scripts for populating the database
- Modular structure for controllers and models

## Project Structure

```
server/
  app.py            # Main Flask app
  config.py         # Configuration settings
  seed.py           # Database seeding script
  controllers/      # API route handlers
  models/           # SQLAlchemy models
migrations/         # Alembic migration scripts
instance/
  late_show.db      # SQLite database (local)
extensions.py       # Custom Flask extensions
requirements.txt    # Python dependencies
```

## Setup

1. **Clone the repository**

    ```sh
    git clone <repo-url>
    cd late-show-api-challenge
    ```

2. **Create and activate a virtual environment**

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set environment variables**

    ```sh
    export FLASK_APP=server/app.py
    export FLASK_ENV=development
    ```

5. **Initialize the database**

    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6. **Seed the database (optional)**

    ```sh
    python server/seed.py
    ```

7. **Run the server**

    ```sh
    flask run
    ```

## Database Migrations

- **Create migration repository:**  
  `flask db init`
- **Generate migration:**  
  `flask db migrate -m "Message"`
- **Apply migrations:**  
  `flask db upgrade`
- **Downgrade:**  
  `flask db downgrade`

## API Documentation

See [`challenge-4-lateshow.postman_collection.json`](challenge-4-lateshow.postman_collection.json) for example requests.
