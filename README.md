# Radii

[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Updates](https://pyup.io/repos/github/pknn1/radii/shield.svg)](https://pyup.io/repos/github/pknn1/radii/)
[![Python 3](https://pyup.io/repos/github/pknn1/radii/python-3-shield.svg)](https://pyup.io/repos/github/pknn1/radii/)
[![CircleCI](https://img.shields.io/circleci/project/github/pknn1/radii.svg)](https://circleci.com/gh/pknn1/radii)
![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Site status](https://img.shields.io/website-up-down-green-red/http/radii.devinpeace.com.svg?label=radii%20is)](https://radii.devinpeace.com)  
Find a new circle, around you.

## Team member
| Name | Github Repository
|:--|:--
|Pakanon Pantisawat| [@pknn1](https://github.com/pknn1) 
|Thanapoom Rattanathumawat| [@poom201211](https://github.com/poom201211)
|Supaluk Jaroensuk| [@SupalukBenz](https://github.com/SupalukBenz)


## Build setup

Activate virtual environment and install required dependencies.
```sh
# Activate virtual environment
# For linux and macO
. venv/bin/activate

```
You can use your own database (mysql) or using default sqlite to do the work.
```sh
# Config Database path (mysql)
export DATABASE_URL=postgresql://localhost/radii_app
```

Migrate and upgrade database to match the models structure
```sh
flask db init
flask db migrate
flask db upgrade
```

Running app in development or Production
**Application will required ssl certificate in order to work correctly.**
```sh
# Development run
python app.py

# Production run
gunicorn app:app --bind 127.0.0.1:5000 --workers=2 --worker-class="egg:meinheld#gunicorn_worker"
```



## Iteration plan and Task board
Iteration plan and task board can be found in [Project's Wiki](https://github.com/pknn1/radii/wiki/Radii).


## Issue Tracker
All of the issue accoring to this project can be found [here](https://github.com/pknn1/radii/issues).


