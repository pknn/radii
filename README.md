# Radii

![CircleCI](https://img.shields.io/circleci/project/github/pknn1/radii.svg)
![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)
![Closed Issue](https://img.shields.io/github/issues-closed-raw/badges/shields.svg)
![Site status](https://img.shields.io/website-up-down-green-red/http/radii.devinpeace.com.svg?label=my-website)
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
gunicorn app:app --workers=2 --worker-class="egg:meinheld#gunicorn_worker"
```