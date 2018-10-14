#!/bin/bash 

docker build -t radii-app:latest .
docker tag radii-app devinpeace/radii-app:latest
docker login -u $DOCKER_LOGIN -p $DOCKER_PWD
docker push devinpeace/radii-app