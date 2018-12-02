# Radii

[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Updates](https://pyup.io/repos/github/pknn1/radii/shield.svg)](https://pyup.io/repos/github/pknn1/radii/)
[![Python 3](https://pyup.io/repos/github/pknn1/radii/python-3-shield.svg)](https://pyup.io/repos/github/pknn1/radii/)
[![CircleCI](https://img.shields.io/circleci/project/github/pknn1/radii.svg)](https://circleci.com/gh/pknn1/radii)
![MIT](https://img.shields.io/github/license/mashape/apistatus.svg)
![Site status](https://img.shields.io/website-up-down-green-red/http/www.devinpeace.com.svg?label=my-website)  

## Team member
| Name | Github 
|:--|:--
|Pakanon Pantisawat| [@pknn1](https://github.com/pknn1) 
|Thanapoom Rattanathumawat| [@poom201211](https://github.com/poom201211)
|Supaluk Jaroensuk| [@SupalukBenz](https://github.com/SupalukBenz)

## Project Description
Radii is a event recommender powered by Cafeine, which is a API service for recommendation based on [Implicit Collaborative filtering Library](https://github.com/benfred/implicit).

## About Cafeine
Cafeine is a API service for recommendation based on [Implicit Collaborative Filtering Library](https://github.com/benfred/implicit), which is an algorithm for predicting user behavior based on their preferences.

Read more about Collaborative Filtering on [How Does Spotify Know You So Well?](https://medium.com/s/story/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe) and [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering).

## Development stacks

- [Flask](http://flask.pocoo.org) as a python framework for Web Application.
- [Jinja Template](http://jinja.pocoo.org) as a Template engine.
- [Flask Dance](https://flask-dance.readthedocs.io/) as an OAuth Library.
- [CircleCI](https://circleci.com) for Continuous Integration platform.
- [Docker](https://www.docker.com) for Container system.
- [Google Cloud Platform](https://cloud.google.com) for hosting.


## Build setup

Activate virtual environment and install required dependencies.
**Linux and macOS**
```sh
. venv/bin/activate
pip install -r requirements.txt
```
**Windows**
```sh
/venv/bin/activate
pip install -r requirements.txt
```
***Optional***  
You can use **your own postgres client database or using default sqlite** to do the work.
```sh
# Config Database path (postgres)
export DATABASE_URL=postgresql://localhost/radii_app    
```

Updating database to match data structure.
```sh
flask db init
flask db migrate
flask db upgrade
```

Running app in Development or Production using [Gunicorn Meinheld](https://gunicorn.org) as a worker class
**Application will required ssl certificate in order to work correctly.**
```sh
# Development run
python app.py

# or if you have flask installed
export FLASK_APP=app.py
flask run

# Production run
gunicorn app:app --bind 127.0.0.1:5000 --workers=2 --worker-class="egg:meinheld#gunicorn_worker"
```

## Developer Resources

* Iteration plans  in [project wiki](https://github.com/pknn1/radii/wiki/Radii).  
* Task board  on [Trello](https://trello.com/b/MqvcS352).
* Design template in [Radii Design Template](https://xd.adobe.com/view/2bf8f25a-cc18-4889-780f-fb2bb66b1028-5dc9/?fullscreen).
* Issues are in Github issuec tracker [here](https://github.com/pknn1/radii/issues).
