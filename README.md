# Employee-churn-classification

## About 
An employee churn classification model is invaluable for organizations seeking to retain their valuable workforce and maintain operational efficiency. It helps predict which employees are at risk of leaving the company, enabling proactive intervention through targeted strategies. This project aims to create a classification model that can help in classifying employee churn. 

## Summary 
Data visualization | Model building | Model deployment 

## How to run? 
**Run locally**
1. Run `docker pull python:3.10.4-slim` to download the python image image from the Docker Hub registry to local machine. 
2. Run `docker build -t <name>:<tag-optional> .` to build docker image.
3. Run `docker run -it -p <port>:<port> <name>:<tag-optional>` to build docker image. Can use 8081 as port if available in system. 

**Deploy**
1. On the same folder, run `eb init -p docker <name>` to initialize an Elastic Beanstalk environment for a Docker application. Make sure an AWS account has been created as `aws-access-id` and `aws-secret-key` would be prompted.
2. Run `eb create <name>` to create a new environment the application. 
3. Run `eb terminate <name>` to stop and delete existing Elastic Beanstalk environment after finish testing.

## Links 
Dataset: [Employee dataset](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset/data)

