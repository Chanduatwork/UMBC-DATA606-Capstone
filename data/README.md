# UMBC-DATA606-Capstone Data
## UCI HAR Dataset – Data Repository

This folder contains the raw data used in the Semi-Supervised Human Activity Recognition (HAR) project. The dataset was collected using smartphone sensors and is structured in a way that supports reproducible machine learning experiments.

## Dataset Source

- **Name:** Human Activity Recognition Using Smartphones
- **Published by:** University of Genoa, Italy
- **Original Link:** [https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
- **Cite as:**  
  Anguita, D., Ghio, A., Oneto, L., Parra, X., & Reyes-Ortiz, J. L. (2013).  
  A Public Domain Dataset for Human Activity Recognition Using Smartphones. ESANN.

## Data Summary

- **Subjects:** 30 individuals (aged 19–48)
- **Activities (6 total):**
  - 1: WALKING
  - 2: WALKING_UPSTAIRS
  - 3: WALKING_DOWNSTAIRS
  - 4: SITTING
  - 5: STANDING
  - 6: LAYING
- **Sampling Rate:** 50 Hz (2.56-second sliding windows with 50% overlap)
- **Total Observations:** 10,299
  - **Training Set:** 7,352 samples
  - **Test Set:** 2,947 samples
- **Features:** 561 features per sample  
  (time/frequency domain signals from accelerometer and gyroscope)

## Folder Structure
## UCI HAR Dataset – Directory Structure

```
UCI HAR Dataset/
│
├── activity_labels.txt        # Mapping of activity IDs to descriptive activity names
├── features.txt               # List of 561 sensor feature names (used as column names)
│
├── train/
│   ├── X_train.txt            # Training feature set (7352 samples × 561 features)
│   ├── y_train.txt            # Activity labels for training set
│   └── subject_train.txt      # Subject IDs corresponding to training samples
│
└── test/
    ├── X_test.txt             # Test feature set (2947 samples × 561 features)
    ├── y_test.txt             # Activity labels for test set
    └── subject_test.txt       # Subject IDs corresponding to test samples
```



## Usage in Project

- The dataset is used to simulate **real-world semi-supervised scenarios**, where only a small fraction of labels (e.g., 5%) are known.
- The remaining unlabeled data is handled using **pseudo-labeling** and **confidence thresholds**.
- Feature scaling, EDA (PCA, t-SNE), and SSL methods are applied on top of this raw data structure.




