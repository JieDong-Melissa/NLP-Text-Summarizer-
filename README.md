# End to End NLP-Text-Summarizer Project

## Tables of Contents
* Background
* Install
* Workflows
* Deployment

## Background

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

# How to run
### STEPS:
Clone the repository 
'''bash
    https://github.com/JieDong-Melissa/NLP-Text-Summarizer-.git
'''

STEP 01- Create a conda environment after opening the repository
    conda create -n summary python=3.8 -y
    conda activate summary

### STEP 02- Install the requirements
'''bash
    pip install -r requirements.txt
'''
       - Finally run the following command
    python app.py

Now,
    open up you local host and port

    Author: Jie Dong
    Data Scientist
    Email: jie.dong@sjsu.edu


# AWS-CI/CD-Deployment-with-Github-Action
## 1. Login to AWS console.
## 2. Create IAM user for deployment
    #with specific access
    1. EC2 access: It is virtual machine
    2. ECR: Elastic Container Registry to save docker image in AWS.

    #Description: About the deployment
    1. Build docker image of the source code
    2. Push your docker image to ECR


    #Policy:
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
    - Save the URI:

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:
    #optional
    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as self-hosted runner (connect github with EC2 machine):
    setting > actions > runner > new self hosted runner > choose os/linux > then run command one by one

## 7. Setup github secrets:
    AWS_ACCESS_KEY_ID: 
    AWS_SECRET_ACCESS_KEY
    AWS_REGION
    AWS_ECR_LOGIN_URI
    ECR_REPOSITORY_NAME