#!/bin/bash 
scp -o "StrictHostKeyChecking no" docker-compose.yml pakanon@35.193.135.74:~/
ssh -o "StrictHostKeyChecking no" pakanon@35.193.135.74 "sudo docker-compose pull && sudo docker-compose up -d"