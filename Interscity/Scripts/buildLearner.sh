#!/bin/bash
export PROJECT_ID=kubernetes-pfc
export DANA_HOME=/home/luizgustavomattoswow/Interscity/dana
PATH=$PATH:$DANA_HOME
cd ../interscity_dana_project
dnc make.dn
dana make.o -l configs/build/dc/all_configs/all_configs.config
cd ..
docker build -t gcr.io/${PROJECT_ID}/interscity-learner -f- . < interscity_dana_project/configs/docker/emergent-microservice-all/Dockerfile
docker push gcr.io/${PROJECT_ID}/interscity-learner
kubectl apply -f InterscityLearnerDeployment.yaml
kubectl expose deployment interscity-learner-deployment --type=LoadBalancer --port 2020 --target-port 2020