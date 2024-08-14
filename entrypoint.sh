#!/bin/sh

# Execute database migration
poetry run alembic upgrade head

# Starts app
poetry run uvicorn --host 0.0.0.0 --port 8000 fast_zero.app:app