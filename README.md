# Human Activity Recognition (HAR) Using Semi-Supervised Learning

## Project Overview

This project investigates the application of **Semi-Supervised Learning (SSL)** to the problem of **Human Activity Recognition (HAR)** using smartphone sensor data. Human Activity Recognition aims to classify everyday physical activities—such as walking, sitting, standing, and laying—based on motion signals captured by accelerometers and gyroscopes embedded in mobile devices.

While HAR has traditionally been addressed using fully supervised learning techniques, such approaches rely heavily on large, carefully labeled datasets. In real-world environments, however, acquiring labeled sensor data is both **expensive and impractical**, as it requires manual annotation, synchronized video recording, or controlled laboratory settings. At the same time, smartphones and wearable devices continuously generate massive amounts of **unlabeled sensor data**, creating a significant gap between data availability and label availability.

This project addresses that gap by leveraging **Semi-Supervised Learning**, a paradigm that allows models to learn from a small labeled dataset alongside a much larger unlabeled dataset. By doing so, the model can exploit the underlying structure of the data distribution and improve performance without requiring full supervision.

---

## Motivation for Semi-Supervised Learning

In many real-world machine learning applications, the assumption of fully labeled data does not hold. This is especially true for sensor-based systems, where data collection is easy but labeling is costly. Semi-supervised learning provides a realistic and scalable alternative by enabling models to:

- Learn meaningful representations from unlabeled data
- Reduce dependence on manual labeling
- Adapt better to real-world deployment conditions

In this project, we simulate a realistic scenario by **intentionally masking 95% of the activity labels** in the training data. Only a small fraction of labeled samples is used to train an initial model. The model then generates **high-confidence predictions** on the unlabeled data, which are treated as **pseudo-labels**. These pseudo-labeled samples are incorporated into the training set, allowing the model to learn from a substantially larger dataset while maintaining reliability.

This process reflects how real-world systems can gradually improve over time as more data becomes available, without requiring constant human intervention.

---

## Real-World Relevance

The use of semi-supervised learning in Human Activity Recognition has significant implications across multiple domains:

- **Healthcare and Remote Monitoring**  
  Activity recognition can help monitor patient mobility, detect abnormal behavior, or assess rehabilitation progress. SSL allows such systems to be deployed with minimal labeled data while still benefiting from continuous sensor streams.

- **Wearable and Fitness Applications**  
  Fitness trackers and smartwatches collect large volumes of motion data, but only a small portion is explicitly labeled. SSL enables more personalized and adaptive activity tracking without extensive annotation.

- **Smart Environments and IoT**  
  In smart homes or industrial environments, understanding human movement patterns is essential for safety and automation. Semi-supervised models can adapt to new users and environments with little manual configuration.

- **Scalability and Cost Efficiency**  
  By reducing reliance on labeled data, SSL significantly lowers development and maintenance costs, making HAR systems more scalable and sustainable.

---

## Project Goal

The primary goal of this project is to demonstrate that **semi-supervised learning can achieve strong classification performance even when labeled data is scarce**. By combining exploratory data analysis, dimensionality reduction techniques, and pseudo-labeling strategies, the project showcases how SSL can be practically applied to real-world sensor data and how it compares to traditional supervised baselines.

Overall, this project serves as a practical example of how modern machine learning systems can be designed to **learn efficiently, scale naturally, and operate effectively under real-world constraints**.
