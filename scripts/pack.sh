#!/bin/bash 

docker build -t $IMAGE_NAME:$TAG .
docker tag $IMAGE_NAME devinpeace/$IMAGE_NAME:$TAG
docker login -u $DOCKER_LOGIN -p $DOCKER_PWD
docker push devinpeace/$IMAGE_NAME