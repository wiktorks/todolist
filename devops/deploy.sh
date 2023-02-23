#!/bin/bash
kubectl create ns qa-server-1
kubectl apply -f deployment/server-1-deployment.yml
kubectl create ns qa-server-2
kubectl apply -f deployment/server-2-deployment.yml
kubectl create ns qa-server-3
kubectl apply -f deployment/server-3-deployment.yml
kubectl create ns qa-server-4
kubectl apply -f deployment/server-4-deployment.yml
kubectl create ns qa-server-5
kubectl apply -f deployment/server-5-deployment.yml
kubectl create ns qa-server-6
kubectl apply -f deployment/server-6-deployment.yml
kubectl create ns qa-server-7
kubectl apply -f deployment/server-7-deployment.yml
kubectl create ns qa-server-8
kubectl apply -f deployment/server-8-deployment.yml