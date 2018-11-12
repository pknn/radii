#!/bin/bash 
scp -o "StrictHostKeyChecking no" docker-compose.yml pakanon_pk@$IP:~/
ssh -o "StrictHostKeyChecking no" pakanon_pk@$IP "yes | sudo docker image prune && sudo docker-compose pull && sudo docker-compose up -d --force-recreate"