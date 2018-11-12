# Radii

![CircleCI](https://img.shields.io/circleci/project/github/pknn1/radii.svg)
![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)
![Site status](https://img.shields.io/website-up-down-green-red/http/www.devinpeace.com.svg?label=my-website)  
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
[Link to trello](https://trello.com/b/MqvcS352)

...

## Issue Tracker
All of the issue according to this project can be found [here](https://github.com/pknn1/radii/issues).
