# END to End ML Project Energy Efficiency on Residual Buildings - Vishnu M

## Problem Statement:
Predict and understand the impact of building design features on both heating and cooling energy needs in residential buildings using both traditional and advanced machine learning approaches.
Prediction task is to determine whether a person makes over 50K a year. (Regression problem)

## There are 14 Independent Variables.

relative compactness: continuous.
surface area: continuous.
wall area: continuous.
roof area: continuous.
overall height: continuous.
orientation: continuous.
glazing area: continuous.
glazing area distribution: continuous.

Target Varibale: Average Heating and Colling Load

## Dataset Source Link : 

## Approach of the project
EDA,FE and Model Traing Approach Notebook:
In EDA, I have created an deep and clean realtions between every column and made some plots using seaborn and matplotlib.
In FE, I have handled missing values,created a all categorical to numerical columns.
I have trained the model using classification algorithms, the best model found is Logistic Regresssion with 85% accuracy.
Link: Model training Notebook

## Modular Code steps:
### Data Ingestion :

In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.

### Data Transformation :

In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median ,then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.

### Model Training :

In this phase base model is tested . The best model found was Logistic Regression.
This model is saved as pickle file.

### Prediction Pipeline :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

### Flask App creation :

Flask app is created with User Interface to predict the Census Income price wheather <=50K or >50K inside a Web Application.

### Deployment:
AWS ECR:
AWS ECR link: http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/

### AWS CI/CD:
Docker image + Github action + AWS EC2 + ECR Repo + App Runner

### steps:
Docker Build checked
Github Workflow
Iam User In AWS
Docker Setup In EC2 commands to be Executed

# optinal

sudo apt-get update -y

sudo apt-get upgrade

# required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

Configure ECR as self-hosted runner:

Setup github secrets: AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
