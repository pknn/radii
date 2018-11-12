#!/bin/bash 
scp -o "StrictHostKeyChecking no" docker-compose.yml pakanon@$IP:~/
ssh -o "StrictHostKeyChecking no" pakanon@$IP "yes | sudo docker image prune && sudo docker-compose pull && sudo docker-compose up -d --force-recreate"