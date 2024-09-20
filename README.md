📘# Pakistan General Election Voters Turnout Prediction

This repository contains a comprehensive machine learning project aimed at predicting voter turnout in Pakistan’s General Elections using historical data from 1970 to 2018. The project involves several stages of data preprocessing, feature engineering, and model development. The goal is to create an accurate predictive model using various machine learning techniques and methodologies.

## Dataset

The dataset used for this project can be accessed from [Kaggle](https://www.kaggle.com/datasets/tahminashoaib86/pakistan-general-elections-dataset-1970-2018?resource=download). It contains detailed electoral results from the past 10 general elections in Pakistan, providing constituency-wise and year-wise data.

### Dataset Description:
- **Features**: Registered voters, total votes polled, rejected votes, valid votes, candidate-wise vote counts, party affiliations, and geographical details such as province, division, district, and constituency.
- **Target Variable**: Voter turnout percentage in each election.

## Project Workflow

### 1. **Data Preprocessing**
   Preprocessing is essential to clean and prepare the dataset for model training. This includes handling missing values, data transformation, and feature selection.

#### a. **Data Quality Assessment**:
   - Assess the quality of the dataset by checking for missing values and data inconsistencies.
   
#### b. **Data Cleaning**:
   - **Handling Missing Values**: Rows with critical missing values are removed, while other columns are filled with the median value. Duplicate rows are also identified and removed.
   - The cleaned dataset is saved as `cleaned_dataset.csv`.

#### c. **Data Transformation**:
   - **Encoding Categorical Variables**: Categorical columns such as party affiliation and region are one-hot encoded to convert them into numerical values.
   - The transformed dataset is saved as `encoded_dataset.csv`.

#### d. **Data Reduction**:
   - **Feature Selection**: Based on correlation with the target variable (voter turnout), less relevant features are removed, retaining only the most important features.
   - The reduced dataset is saved as `preprocessed_dataset.csv`.

### 2. **Modeling**
   After preprocessing, the dataset is ready for model training. Several steps are taken to build, train, and evaluate machine learning models.

#### a. **Feature and Target Variable Separation**:
   - The features (`X`) are separated from the target variable (`y`), where `y` represents the voter turnout.
   - Irrelevant features such as `Year` and `NA` are dropped from the feature set.

#### b. **Data Splitting for Training and Testing**:
   - The dataset is split into training and testing sets using `train_test_split()`. 70% of the data is used for training, and 30% for testing.

#### c. **Handling Missing Values in Training Set**:
   - Missing values in the training set are handled using the `SimpleImputer` with the mean strategy.

#### d. **Model Training**:
   - A **Linear Regression** model is instantiated and trained using the preprocessed data. The model is trained to predict voter turnout using features such as the number of registered voters, total votes polled, and demographic details.

#### e. **Model Evaluation**:
   - The performance of the model is evaluated using the **R-squared** score to determine how well the model explains the variability of the target variable.
   - Training R-squared: 0.81
   - Testing R-squared: 0.78​

#### f. **Prediction for 2024**:
   - A hypothetical dataset for the year 2024 is created, and the model predicts voter turnout using the trained model.

#### g. **Overall Model Accuracy**:
   - The overall accuracy of the model is calculated as the mean of the training and testing accuracies. Based on the R-squared scores, the model is reasonably accurate in predicting          voter turnout trends, with an average accuracy of 79.5%​

## Usage Instructions

### 1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/Pakistan-General-Election-Voters-Turnout-Prediction.git
   ```

### 2. Install Dependencies:
   The project requires the following libraries:
   - `pandas`
   - `numpy`
   - `scikit-learn`
   - `xgboost`
   
   Install them using the following command:
   ```bash
   pip install pandas numpy scikit-learn xgboost
   ```


## Contributions

Contributions to the project are welcome. If you have any ideas, feel free to open an issue or submit a pull request.

