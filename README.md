# END to End ML Project Energy Efficiency on Residual Buildings - Vishnu M

## Problem Statement:
-Predict and understand the impact of building design features on both heating and cooling energy needs in residential buildings using both traditional and advanced machine learning approaches.

## There are 14 Independent Variables.

-relative compactness: continuous.
-surface area: continuous.
-wall area: continuous.
-roof area: continuous.
-overall height: continuous.
-orientation: continuous.
-glazing area: continuous.
-glazing area distribution: continuous.

Target Varibale: Average Heating and Colling Load

### Dataset Source Link : https://archive.ics.uci.edu/dataset/242/energy+efficiency

### Approach of the project
EDA,FE and Model Traing Approach Notebook:
In EDA, I have created an deep and clean realtions between every column and made some plots using seaborn and matplotlib.
In FE, I have handled missing values,created a all categorical to numerical columns.
I have trained the model using classification algorithms, the best model found is Logistic Regresssion with 85% accuracy.
Link: Model training Notebook

### Modular Code steps:
#### Data Ingestion :

In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.

#### Data Transformation :

In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median ,then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.

#### Model Training :

In this phase base model is tested . The best model found was Logistic Regression.
This model is saved as pickle file.

#### Prediction Pipeline :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

#### Flask App creation :

Flask app is created with User Interface to predict the Census Income price wheather <=50K or >50K inside a Web Application.

#### Deployment:
AWS ECR:
AWS ECR link: [[http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/](https://yxdzqmvtk6.us-west-2.awsapprunner.com/predictdata)]

#### AWS CI/CD:
Docker image + Github action + AWS EC2 + ECR Repo + App Runner

#### steps:
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


# END to End Census Income Predcition - Sandeep Bandi

## Problem Statement:
- The Goal is to predict whether a person has an income of more than 50K a year or not.
- This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.

## Introduction About the Data

Prediction task is to determine whether a person makes over 50K a year. (Classification problem)

There are 14 Independent Variables.
- age: continuous.
- workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- fnlwgt: continuous.- education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate 5th-6th, Preschool.
- education-num: continuous.
- marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct,Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.- sex: Female, Male.
- capital-gain: continuous.
- capital-loss: continuous.
- hours-per-week: continuous.
- native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

Target Varibale:
- income: >50K, <=50K.

Dataset Source Link : https://archive.ics.uci.edu/ml/datasets/census+income

## Approach of the project

### EDA and FE Notebook:
- In EDA, I have created an deep and clean realtions between every column and made some plots using seaborn and matplotlib.
- In FE, I have handled missing values,created a all categorical to numerical columns.

Link: [EDA Notebook](./notebook/EDA.ipynb)

# Model Traing Approach Notebook:
- I have trained the model using classification algorithms, the best model found is Logistic Regresssion with 85% accuracy.

Link: [Model training Notebook](./notebook/model_trainer.ipynb)

## Modular Code steps:

1. Data Ingestion :
   * In Data Ingestion phase the data is first read as csv.
   * Then the data is split into training and testing and saved as csv file.

2. Data Transformation :
   * In this phase a ColumnTransformer Pipeline is created.
   * for Numeric Variables first SimpleImputer is applied with strategy median ,then Standard Scaling is performed on numeric data.
   * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
   * This preprocessor is saved as pickle file.

3. Model Training :
   * In this phase base model is tested . The best model found was Logistic Regression.
   * This model is saved as pickle file.

4. Prediction Pipeline :
   * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation :
   * Flask app is created with User Interface to predict the Census Income price wheather <=50K or >50K inside a Web Application.

# Deployment:

## AWS Elastic Beanstalk link:
AWS ELastic Beanstalk link: [http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/](http://censusincome-env.eba-beuv8ifw.ap-south-1.elasticbeanstalk.com/)

## AWS CI/CD:
### Docker image + Github action + AWS EC2 + ECR Repo

- steps:

1. Docker Build checked
2. Github Workflow
3. Iam User In AWS

- Docker Setup In EC2 commands to be Executed

   #optinal

   sudo apt-get update -y

   sudo apt-get upgrade


   #required

   curl -fsSL https://get.docker.com -o get-docker.sh

   sudo sh get-docker.sh

   sudo usermod -aG docker ubuntu

   newgrp docker



- Configure EC2 as self-hosted runner:
- Setup github secrets:
   AWS_ACCESS_KEY_ID=

   AWS_SECRET_ACCESS_KEY=

   AWS_REGION = us-east-1

   AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

   ECR_REPOSITORY_NAME = simple-app
