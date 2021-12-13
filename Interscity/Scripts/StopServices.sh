#!/bin/bash
kubectl delete service interscity-learner-deployment
kubectl delete deployment interscity-learner-deployment
kubectl delete service metrics-server
kubectl delete pod metrics-server
kubectl delete service mydb
kubectl delete deployment mydb