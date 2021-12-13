#!/bin/bash
export PROJECT_ID=kubernetes-pfc
docker build -t gcr.io/${PROJECT_ID}/metrics-server .
docker push gcr.io/${PROJECT_ID}/metrics-server
kubectl apply -f metricsServerPod.yaml
kubectl expose pod metrics-server --type=LoadBalancer --port 3333 --target-port 3333
