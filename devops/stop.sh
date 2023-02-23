#!/bin/bash
kubectl delete -f deployment/server-1-deployment.yml
kubectl delete -f deployment/server-2-deployment.yml
kubectl delete -f deployment/server-3-deployment.yml
kubectl delete -f deployment/server-4-deployment.yml
kubectl delete -f deployment/server-5-deployment.yml
kubectl delete -f deployment/server-6-deployment.yml
kubectl delete -f deployment/server-7-deployment.yml
kubectl delete -f deployment/server-8-deployment.yml