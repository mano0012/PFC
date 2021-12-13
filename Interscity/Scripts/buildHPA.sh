#!/bin/bash
export PROJECT_ID=kubernetes-pfc
export DANA_HOME=/home/luizgustavomattoswow/Interscity/dana
PATH=$PATH:$DANA_HOME
cd ../interscity_dana_project
dnc make.dn
dana make.o -l configs/build/dc/cache_compression/cache_compression.config
cd ..
docker build -t gcr.io/${PROJECT_ID}/interscity-hpa -f- . < interscity_dana_project/configs/docker/emergent-microservice-hpa/Dockerfile
docker push gcr.io/${PROJECT_ID}/interscity-hpa
kubectl apply -f InterscityHPADeployment.yaml
kubectl expose deployment interscity-hpa-deployment --type=LoadBalancer --port 2020 --target-port 2020