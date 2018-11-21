#!/bin/bash 
scp -o "StrictHostKeyChecking no" docker-compose.yml pakanon_pk@$IP:~/radii-app
ssh -o "StrictHostKeyChecking no" pakanon_pk@$IP "cd radii-app && yes | sudo docker image prune && sudo docker-compose pull && sudo docker-compose up -d --force-recreate"