# Feedback to Foresight: Simplifying App Review Sentiment Analysis
## FTDS-009-HCK-group-002
**Members**:
1. Devin Yaung Lee — Data Analyst
2. Fernaldy Aristo Wirjowerdojo — Data Engineer
3. Muhammad Furqon Pakpahan — Data Engineer
4. Sifra Hilda Juliana Siregar — Data Scientist


## Project Overview
This project focuses on performing sentiment analysis on Google Play Store app reviews. Utilizing Natural Language Processing (NLP), the goal is to analyse user feedback to gain insights into satisfaction and app perception.


## Background
### Problem Statement
In the competitive landscape of mobile applications, user feedback for app reviews is a goldmine of insights that can inform product development and marketing strategies. However, these reviews are often unstructured, making it challenging to efficiently extract, categorize, and analyze sentiments and opinions. There is a need for an automated system that can process this feedback to provide actionable insights, identify trends in user sentiment, and highlight areas for improvement. This project aims to address the lack of structured analysis of user-generated content in app reviews on the Google Play Store, which, if leveraged correctly, can significantly enhance user satisfaction and app performance in the market.

### Objectives
- Develop an Automated Sentiment Analysis Model
> Build and train a TensorFlow model to classify app reviews into positive, negative, and neutral sentiments with high accuracy.
- Understand the user feedbacks in depth
    - Utilize the sentiment analysis model to delve into the nuances of user feedback on the Google Play Store

### Dataset
The dataset used in this project is obtained from Kaggle from [this link](https://www.kaggle.com/datasets/whenamancodes/play-store-apps?select=googleplaystore.csv).


## Project Structure
### Workflow
The workflow is split into 3, separated by roles:
#### Data Engineering
- **Data Collection**: Raw data is stored in an AWS S3 bucket
- **Data Cleaning**: An Apache Airflow DAG is set up to fetch and clean the data
- **Data Storage**: Cleaned data is stored back into an S3 bucket

#### Data Science
- **Model Development**: Using the cleaned data from the S3 bucket, a TensorFlow regression model is created to perform sentiment analysis
- **Model Optimization**: Tuning and optimization of the model for better accuracy

#### Data Analysis
- **Data Interpretation**: Analyze the results from the model to understand user sentiment
- **Visualization**: Create visual representations of the analysis for easier interpretation and presentation
- **Reporting**: Compile findings and insights into a comprehensive report

## Stack
- **Docker**: To containerize and package all the process done for data pipeline to ensure reproducibility
- **Apache Airflow**: For orchestrating and automating the data pipeline
- **AWS S3**: For data storage and retrieval
- **TensorFlow**: For building and training the sentiment analysis model
- **Python**: Primary programming language used for data processing and analysis


## Setup and Installation
To replicate this project, there are multiple prerequisites that you need to have:
1. AWS account and IAM user with access to S3 bucket: The bucket has to contain the two files which can be downloaded from [Dataset](#dataset)
2. Docker
3. Python
4. Environment Configuration: `.env` file for the airflow containers to get access to the S3 bucket
> For security reasons, the `.env` file is included but not completed

To replicate this project assuming you have all of the prerequisites above:
1. Clone this repo
```bash
git clone git@github.com:devinlee14/FTDS-009-HCK-group-002.git
```
2. Compose the containers
```bash
cd FTDS-009-HCK-group-002
docker-compose up -d
```
3. Access the airflow webserver and setup the airflow credentials for S3
4. Trigger the DAG
5. Download the cleaned data from S3
6. Run the `EDA_model.ipynb` file to create the models

Alternatively, all the models are in the repo (`lstm`, `cnn` and `gru`) for you to use and we also have a deployed model on [Huggingface](#Huggingface_link).