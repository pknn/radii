# Radii

> Find a new circle, around you.

## Build setup

```sh
# Generate virtual environment
python3 -m venv venv
. venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Config Database path
export DATABASE_URL=mysql+pysql://username:password@host/database

# Development run
python app.py

# Production run
gunicorn app:app
```