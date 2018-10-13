#!/bin/bash 

docker build -t radii:latest .
docker tag radii devinpeace/radii:latest
docker push devinpeace/radii:latest