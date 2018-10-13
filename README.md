# Radii

> Find a new circle, around you.

## Build setup

```sh
# Generate virtual environment
python3 -m venv venv
. venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Development run
python app.py

# Production run
gunicorn app:app
```