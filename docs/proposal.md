# Semi-Supervised Human Activity Recognition (HAR)

## Title and Author

**Project Title:** Semi-Supervised Human Activity Recognition (HAR)  

**Prepared for:** UMBC Data Science Master’s Degree Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  

**Author:** Chandu Vemmasani  

- **GitHub Repository:** [https://github.com/Chanduatwork/UMBC-DATA606-Capstone]  
 

## Background

### What is it about?
Smartphone sensors, such as accelerometers and gyroscopes, are used in Human Activity Recognition (HAR) to identify daily human activities, like walking, sitting, standing, or laying. Instead, motion features are obtained from these signals that can be used by machine learning models to classify an activity. In the past, Human Activity Recognition has utilized supervised learning where models are trained on large amounts of labeled data of activity.

### Why does it matter?
Accurate Human Activity Recognition (HAR) can be invaluable in sectors such as healthcare (e.g. monitoring elderly patients, fall detection, chronic disease management), fitness tracking (e.g. step-counting), workplace safety (e.g. inspection), and human-computer interaction (e.g. context detection). However, labeling activity data is costly, time-consuming, and often cannot be done at scale. In contrast, smartphones are generating many gigabytes of unlabeled sensor data every day. This dichotomy of labeled data and unlabeled data creates an incentive to use Semi-Supervised Learning (SSL), which can utilize both types of data to build more accurate and cost-effective models. 
### Research Questions
1. Can semi-supervised learning methods, such as Label Spreading and Self-Training, improve classification performance when only a small percentage of labeled data is available?  
2. How do SSL methods compare against traditional supervised learning baselines when trained with limited labels?  
3. Which SSL method is more effective for HAR, considering the cluster structure of the dataset?  
4. What insights can exploratory data analysis (PCA, t-SNE) provide about the natural clustering of activities and their suitability for SSL?  

## Dataset Description

### Data Sources
- **Dataset:** UCI Human Activity Recognition (HAR) Using Smartphones  
- **Source:** UCI Machine Learning Repository  
- **Collection:** Data gathered from 30 volunteers (aged 19–48 years) carrying a smartphone (Samsung Galaxy S II) on the waist.  

### Data Size
- Memory usage in pandas: ~44 MB  
- Shape: 10,299 rows × 563 columns  

### Time Period
- Not time-bound across years; instead, the dataset was collected in controlled experiments where each subject performed activities over a few minutes per session.  

### Row Representation
- Each row corresponds to a **single observation**: a set of 561 features derived from accelerometer and gyroscope signals at **30 Hz frequency**, for a particular subject performing one activity.  

### Data Dictionary
- **Subject (int64):** ID of the volunteer (1–30).  
- **Activity (object):** Target variable with 6 categories:  
  - WALKING  
  - WALKING_UPSTAIRS  
  - WALKING_DOWNSTAIRS  
  - SITTING  
  - STANDING  
  - LAYING  
- **561 features (float64):** Sensor-derived measurements from time and frequency domains. Examples include:  
  - `tBodyAcc-mean()-X`: Mean body acceleration in the X direction.  
  - `tBodyAcc-std()-Y`: Standard deviation of body acceleration in the Y direction.  
  - `tBodyAcc-max()-Z`: Maximum value of body acceleration in the Z direction.  
  - Features cover multiple statistical measures (mean, std, mad, max, min, energy, etc.) across 3 axes (X, Y, Z).  

### Variables for Modeling
- **Target/Label:** `Activity`  
- **Predictors/Features:** All 561 numerical sensor-based features.  
- **Exclusions:** `Subject` column will not be used as a predictor, but may help with analysis (e.g., subject-level generalization).  
