# Radii

![CircleCI](https://img.shields.io/circleci/project/github/pknn1/radii.svg)
![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)
![Site status](https://img.shields.io/website-up-down-green-red/http/radii.devinpeace.com.svg?label=my-website)  
Find a new circle, around you.

## Team member
| Name | Github Repository |
|:--|:--|
|Pakanon Pantisawat| [@pknn1](https://github.com/pknn1)
|Thanapoom Rattanathumawat| [@poom201211](https://github.com/poom201211)
|Supaluk Jaroensuk| [@SupalukBenz](https://github.com/SupalukBenz)


## Build setup

Activate virtual environment and install required dependencies.
```sh
# Activate virtual environment
# For linux and macOS
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
You can use your own database (mysql) or using default sqlite to do the work.
```sh
# Config Database path (mysql)
export DATABASE_URL=mysql+pysql://username:password@host/database
```

Running app in development or Production

```sh
# Development run
python app.py

# Production run
gunicorn app:app --workers=2 --worker-class="egg:meinheld#gunicorn_worker"
```



## Iteration plan and Task board
Iteration plan and task board can be found in [Project's Wiki](https://github.com/pknn1/radii/wiki/Radii).

...

## Issue Tracker
All of the issue accoring to this project can be found [here](https://github.com/pknn1/radii/issues).


