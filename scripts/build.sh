#! /bin/bash

docker-compose down --rmi all
docker-compose pull
docker-compose build