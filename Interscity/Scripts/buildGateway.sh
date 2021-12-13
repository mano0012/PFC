#!/bin/bash
export PROJECT_ID=kubernetes-pfc
export DANA_HOME=/home/luizgustavomattoswow/Interscity/dana
PATH=$PATH:$DANA_HOME
cd ../interscity_dana_project
dnc make.dn
dana make.o -l configs/build/dc/all_configs/all_configs.config
cd ..
docker build -t gcr.io/${PROJECT_ID}/hpa-gateway -f- . < interscity_dana_project/configs/docker/HPA-Gateway/Dockerfile
docker push gcr.io/${PROJECT_ID}/hpa-gateway
kubectl apply -f HPA-Gateway.yaml
kubectl expose pod hpa-gateway --type=LoadBalancer --port 5555 --target-port 5555