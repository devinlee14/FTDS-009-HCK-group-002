# Google Play Store Apps Sentiment Analysis
## FTDS-009-HCK-group-002
**Members**:
1. 
2.
3.
4.

## Project Overview
This project focuses on performing sentiment analysis on e-commerce product reviews. Utilizing Natural Language Processing (NLP), the goal is to analyse customer feedback to gain insights into customer satisfaction and product perception.


## Background
### Problem Statement

### Objectives
- 
-
-

### Dataset
The dataset used in this project is obtained from Kaggle from [this link](https://www.kaggle.com/datasets/whenamancodes/play-store-apps?select=googleplaystore.csv).


## Project Structure
### Workflow
The workflow is split into 3, separated by roles:
#### Data Engineering
- **Data Collection**: Raw data is stored in an AWS S3 bucket.
- **Data Cleaning**: An Apache Airflow DAG is set up to fetch and clean the data.
- **Data Storage**: Cleaned data is stored back into an S3 bucket.

#### Data Science
- **Model Development**: Using the cleaned data from the S3 bucket, a TensorFlow regression model is created to perform sentiment analysis.
- **Model Optimization**: Tuning and optimization of the model for better accuracy.

#### Data Analysis
- **Data Interpretation**: Analyze the results from the model to understand customer sentiment.
- **Visualization**: Create visual representations of the analysis for easier interpretation and presentation.
- **Reporting**: Compile findings and insights into a comprehensive report.

#### Technologies Used / Stack
- **Apache Airflow**: For orchestrating and automating the data pipeline.
- **AWS S3**: For data storage and retrieval.
- **TensorFlow**: For building and training the sentiment analysis model.
- **Python**: Primary programming language used for data processing and analysis.

## Setup and Installation
To replicate this project, there are multiple prerequisites that you need to have:
1. AWS account and IAM user with access to S3 bucket: The bucket has to contain the two files which can be downloaded from [Dataset](#dataset).
2. Docker
3. Python
4. Environment Configuration: `.env` file for the airflow containers.
> (For security reasons, the `.env` file is not included in the repository)

To run the project assuming you have all of the prerequisites above you can run these commands
```bash
git clone git@github.com:devinlee14/FTDS-009-HCK-group-002.git
cd FTDS-009-HCK-group-002
docker-compose up -d
```
