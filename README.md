# Anemia Classification Project: A Comparative Analysis of Classification Algorithms

## Overview
This project focuses on classifying individuals based on the types of anemia they exhibit. Anemia, a common blood disorder, can manifest in various forms, each with distinct hematological characteristics. Accurate classification aids in personalized treatment and management strategies.


## Dataset
The dataset used in this project is "diagnosed_cbc_data_v4.csv," sourced from Kaggle. It contains clinical data from diagnosed individuals, including various hematological parameters such as red blood cell count, hemoglobin levels, and mean corpuscular volume (MCV), along with the target variable indicating the presence or absence of anemia.The dataset can be accessed [https://www.kaggle.com/datasets/ehababoelnaga/anemia-types-classification]

## Preprocessing Steps
1. **Duplicate Removal**: Duplicated records were identified and removed from the dataset.
2. **Exploratory Data Analysis (EDA)**: Automated exploratory data analysis was performed using the Sweetviz library to gain insights into the dataset's structure and distributions.
3. **Outlier Treatment**: Outliers in the numerical features were identified and treated using Winsorization.
4. **Normalization**: Min-Max scaling was applied to normalize the numerical features to a common scale.
5. **Label Encoding**: The target variable indicating anemia status was label-encoded for model training.

## Models Evaluated
Several classification algorithms were evaluated to predict anemia status. The models used are:
- Logistic Regression
- Best Logistic Regression (using RandomizedSearchCV)
- Decision Tree Classifier
- Best Decision Tree (using RandomizedSearchCV)
- Random Forest Classifier
- Best Random Forest (using RandomizedSearchCV)
- Ensemble Method (Voting Classifier)
- Best Ensemble Method (using RandomizedSearchCV)

## Evaluation Metrics
The performance of each model was evaluated using the following metrics:
- Accuracy Score
- Classification Report (Precision, Recall, F1-score)
- Confusion Matrix

## Results
The performance of the models on the test set is summarized below:


| Algorithm                | Train Accuracy | Test Accuracy |
|--------------------------|----------------|---------------|
| Logistic Regression      | 0.863959       | 0.793522      |
| Best Logistics Regression| 0.901523       | 0.834008      |
| Decision Tree            | 1.000000       | 0.959514      |
| Best Decision Tree       | 0.996954       | 0.963563      |
| Random Forest            | 1.000000       | 0.959514      |
| Best Random Forest       | 0.991878       | 0.955466      |
| Ensemble Method          | 1.000000       | 0.951417      |
| Best Ensemble Method     | 0.993909       | 0.963563      |

## Conclusion
- The Decision Tree, Best Random Forest, and Best Ensemble Method achieved the highest accuracy on the test set, indicating their strong performance in predicting anemia status.
- All models performed well, but the use of RandomizedSearchCV for hyperparameter tuning improved the performance of several models.
- Further optimization and fine-tuning of hyperparameters may enhance model performance.

## Future Work
- Explore additional feature engineering techniques to improve model performance.
- Investigate the potential of deep learning models for anemia classification.
- Conduct further analysis to understand the factors contributing to false positives/negatives.


