# UMBC-DATA606-Capstone NoteBook
## Semi-Supervised Learning for Human Activity Recognition (HAR)

This Jupyter Notebook demonstrates how to perform Human Activity Recognition (HAR) using semi-supervised learning methods on the UCI HAR dataset. The notebook takes you through the complete data science pipeline — from data preprocessing to model training, pseudo-labeling, evaluation, and final deployment.

## What the Notebook Includes

- Data loading and cleaning  
  - Reads raw sensor data from the accelerometer and gyroscope
  - Ensures feature name uniqueness and merges training/testing sets
  - Maps numeric activity labels to descriptive names

- Exploratory Data Analysis (EDA)  
  - Distribution of activities and subject IDs  
  - Summary statistics of features  
  - Correlation heatmaps and feature visualizations  
  - PCA and t-SNE projections to explore clustering of activities

- Baseline Supervised Learning  
  - Trains models (Random Forest, Logistic Regression) using only 5% labeled data  
  - Evaluates accuracy and class-wise performance on the test set

- Semi-Supervised Learning with Pseudo-Labeling  
  - Masks 95% of labels to simulate a low-label environment  
  - Uses high-confidence predictions from the baseline model to assign pseudo-labels  
  - Combines pseudo-labeled and real-labeled data to retrain and improve the model

- Final Model Training and Export  
  - Builds a reusable scikit-learn pipeline  
  - Trains a Logistic Regression model on the expanded dataset  
  - Evaluates final test performance  
  - Saves the trained model for deployment using joblib

## Why This Matters

Labeling sensor data is expensive and time-consuming. In real-world HAR scenarios (e.g., health monitoring, fitness tracking, smart environments), large amounts of unlabeled data are available, but only a small portion can be labeled manually. This notebook shows how to leverage that unlabeled data using semi-supervised learning to build scalable and accurate activity recognition systems.

## Dataset

- UCI Human Activity Recognition Using Smartphones Dataset  
- 30 volunteers performed six activities while carrying a smartphone  
- Dataset contains 561 features extracted from motion signals

## Outcomes

- Demonstrates effective use of semi-supervised learning in low-label scenarios  
- Achieves over 90% test accuracy using a combination of real and pseudo-labeled data  
- Ready-to-use pipeline for real-time HAR applications
