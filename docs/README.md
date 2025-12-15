
# Semi-Supervised Human Activity Recognition (HAR)

## Title and Author

**Project Title:** Semi-Supervised Human Activity Recognition (HAR)  
**Prepared for:** UMBC Data Science Master’s Degree Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  
**Author:** Chandu Vemmasani  

- **GitHub Repository:** [https://github.com/Chanduatwork/UMBC-DATA606-Capstone](https://github.com/Chanduatwork/UMBC-DATA606-Capstone)  
- **Presentation Slides:** [https://github.com/Chanduatwork/UMBC-DATA606-Capstone/blob/main/docs/finalppt.pptx]  
- **YouTube Video:** [https://youtu.be/YYbM8CCp6_4]  

---

##  Project Overview

Human Activity Recognition (HAR) using smartphone sensor data has become essential in healthcare monitoring, fitness tracking, workplace safety, and smart human-computer interaction. Traditional models rely on fully labeled datasets; however, acquiring labeled data at scale is costly and time-consuming. This project demonstrates a **Semi-Supervised Learning (SSL)** approach to HAR using the UCI HAR dataset. The key idea is to leverage a small fraction of labeled data (~5%) and a large amount of unlabeled data through pseudo-labeling techniques to build effective activity classifiers.

---

##  Dataset Overview

- **Dataset:** UCI Human Activity Recognition (HAR) Using Smartphones  
- **Source:** UCI Machine Learning Repository  
- **Subjects:** 30 individuals (ages 19–48) wearing a smartphone on the waist  
- **Sampling Rate:** 30Hz (samples per second)  
- **Features:** 561 time and frequency domain features  
- **Target Activities (6):**  
  - WALKING  
  - WALKING_UPSTAIRS  
  - WALKING_DOWNSTAIRS  
  - SITTING  
  - STANDING  
  - LAYING  
- **Shape:** 10,299 rows × 563 columns  
- **Train/Test Split:**  
  - Train: 7352 samples  
  - Test: 2947 samples  

---

##  Technical Workflow

### 1. **Data Preparation**
- Parsed `features.txt`, `activity_labels.txt`, and training/testing data.
- Ensured all 561 feature names were made unique to avoid column duplication.
- Mapped activity IDs to meaningful labels for interpretability.

### 2. **Exploratory Data Analysis (EDA)**
- Inspected class and subject distributions.  
- Generated boxplots, histograms, correlation heatmaps, and pairwise scatter plots.  
- Used PCA and t-SNE for dimensionality reduction and to assess the natural separability of activity clusters.

 _Sample EDA Visuals_:  
![Activity Distribution](1box.png)  
![Boxplot of tBodyAcc-mean-X](tbmbox.png)  
![Histogram of tBodyAcc-mean-X](hist.png)  
![Heatmap](corelation.png)  
![PCA](PCA.png)  
![t-SNE](tsne.png)  

### 3. **Preprocessing**
- Standardized the features using `StandardScaler` to ensure all features contribute equally.
- Created a labeled/unlabeled mask by randomly keeping only 5% of training labels and setting the rest as `-1`.

### 4. **Baseline Supervised Learning**
- Trained a `RandomForestClassifier` using only the labeled subset (5%).
- Evaluated test accuracy and confusion matrix.

### 5. **Pseudo-Labeling (Self-Training)**
- Predicted class probabilities for unlabeled data.
- Selected only those with high-confidence predictions (threshold ≥ 0.95).
- Added pseudo-labeled samples back to the training set.

### 6. **Final Training (SSL Enhanced Model)**
- Trained an expanded model using both original and pseudo-labeled data.
- Evaluated improved accuracy, precision, recall, and F1-score.
- Compared performance of `RandomForestClassifier` and `LogisticRegression`.

---

##  Evaluation Summary

| Model | Accuracy (Labeled Only) | Accuracy (After Pseudo-Labeling) |
|-------|--------------------------|----------------------------------|
| Random Forest | 0.869 | 0.861 |
| Logistic Regression | 0.896 | 0.895 |
| Final Pipeline (SSL) | — | **0.906**  |

 _Final Confusion Matrix:_  
![Confusion Matrix](matrix.png)

---

##  Streamlit App (Deployed Locally)

A lightweight Streamlit web app was created to demonstrate the end-to-end classification. The user can:
- Upload sensor feature data as `.csv`
- View predicted activity for each sample
- Display model metrics and confidence

 _Screenshots of Streamlit App:_  
![App Upload](Slidder.png)  
![App Prediction](CSV.png)  

---

##  Why Semi-Supervised Learning?

Semi-supervised learning helps bridge the gap between limited labeled data and abundant unlabeled data. In real-world HAR scenarios:
- Manual labeling is costly and labor-intensive.
- Unlabeled sensor data is easy to collect (smartphones, wearables).
- SSL enables rapid model development with reduced labeling effort.

This project demonstrates that **self-training with high-confidence pseudo-labeling** can achieve near-supervised accuracy with just 5% of labeled data — highlighting SSL's real-world applicability.

---

##  Repository Structure
```
UCI HAR Dataset/
├── activity_labels.txt # Mapping of activity IDs to names
├── features.txt # List of all 561 feature names
├── train/
│ ├── X_train.txt # Training features (7352 × 561)
│ ├── y_train.txt # Activity labels
│ └── subject_train.txt # Subject IDs for training
├── test/
│ ├── X_test.txt # Test features (2947 × 561)
│ ├── y_test.txt # Activity labels
│ └── subject_test.txt # Subject IDs for test samples

```

---

##  Key Takeaways

- SSL models can significantly reduce annotation cost while achieving high performance.
- HAR datasets are naturally well-suited for cluster-based methods like t-SNE and pseudo-labeling.
- Streamlit allows rapid deployment and interaction with HAR models in a user-friendly interface.

---

##  Resources

- [UCI HAR Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
