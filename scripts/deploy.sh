#!/bin/bash 
scp -o "StrictHostKeyChecking no" docker-compose.yml pakanon@35.240.234.173:~/
ssh -o "StrictHostKeyChecking no" pakanon@35.240.234.173 "sudo docker-compose pull && sudo docker-compose up -d --force-recreate"