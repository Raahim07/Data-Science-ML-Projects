# -*- coding: utf-8 -*-
"""DataPreProcessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bj4HcoMjfdcswKD8s_zHTms69bVkkNEA
"""

import pandas as pd
df = pd.read_csv('ElectionData.csv')
df.head()

missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Drop rows with missing values in 'Votes', 'ValidVotes', 'RejectedVotes', 'Regd_Voters', 'Total_Votes', 'Turnout', 'turnout_n', 'Party', 'Party Name', 'Party Cluster'
df.dropna(subset=['Votes', 'ValidVotes', 'RejectedVotes', 'Regd_Voters', 'Total_Votes', 'Turnout', 'turnout_n', 'Party', 'Party Name', 'Party Cluster'], inplace=True)

# Fill missing values in 'Regd_Voters', 'Total_Votes', 'Turnout', and 'turnout_n' with median of respective columns
median_Regd_Voters = df['Regd_Voters'].median()
median_Total_Votes = df['Total_Votes'].median()
median_Turnout = df['Turnout'].median()
median_turnout_n = df['turnout_n'].median()

df['Regd_Voters'].fillna(median_Regd_Voters, inplace=True)
df['Total_Votes'].fillna(median_Total_Votes, inplace=True)
df['Turnout'].fillna(median_Turnout, inplace=True)
df['turnout_n'].fillna(median_turnout_n, inplace=True)

# Save the changes to the dataset
df.to_csv("corrected_dataset.csv", index=False)

df1 = pd.read_csv('corrected_dataset.csv')
missing_values = df1.isnull().sum()
print("Missing Values:\n", missing_values)

duplicates = df1.duplicated()

# Print the duplicate rows
print("Duplicate Rows:\n", df1[duplicates])

num_duplicates = duplicates.sum()
print("\n\nNumber of duplicate rows:", num_duplicates)

# Drop duplicates
df1.drop_duplicates(inplace=True)

# Reset the index
df1.reset_index(drop=True, inplace=True)

# Save the cleaned dataset to a new CSV file
df1.to_csv("cleaned_dataset.csv", index=False)

df2 = pd.read_csv('cleaned_dataset.csv')

duplicates = df2.duplicated()

num_duplicates = duplicates.sum()
print("\n\nNumber of duplicate rows:", num_duplicates)

categorical_columns = ['District', 'Division', 'Province', 'Zone', 'Region', 'Party', 'Party Name', 'Party Cluster']

# Ensure that the specified categorical columns are present in the DataFrame
for col in categorical_columns:
    if col not in df2.columns:
        raise ValueError(f"Column '{col}' is missing in the DataFrame.")

# Encode categorical variables using one-hot encoding
df_encoded = pd.get_dummies(df2, columns=categorical_columns)

# Display the transformed dataframe
df_encoded

df_encoded.to_csv("encoded_dataset.csv", index=False)

df3 = pd.read_csv('encoded_dataset.csv')

# Calculate correlation with 'Turnout'
correlation = df3.corr()['Turnout'].abs().sort_values(ascending=False)

# Select the top n features based on correlation coefficient (excluding the target variable)
n_features = 10  # Adjust the number of features as needed
selected_features = correlation.drop('Turnout').nlargest(n_features).index

# Subset the dataframe with the selected features and the target variable
selected_features = list(selected_features) + ['Turnout']
df_reduced = df3[selected_features]

# Display the reduced dataframe
# df_reduced
df3

df_reduced.to_csv("preprocessed_dataset.csv", index=False)

df4 = pd.read_csv('preprocessed_dataset.csv')
df4

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

# Load the data into a DataFrame
df = pd.read_csv('preprocessed_dataset.csv')

# Drop rows with missing values in specified columns
columns_to_check = ['Votes', 'ValidVotes', 'RejectedVotes', 'Regd_Voters', 'Total_Votes', 'Turnout', 'turnout_n']
df.dropna(subset=columns_to_check, inplace=True)

# Convert all columns to numeric if possible
df = df.apply(pd.to_numeric, errors='coerce')

# Drop any rows with missing values after conversion
df.dropna(inplace=True)

# Split the data into features (X) and target variable (y)
X = df.drop(columns=['Turnout'])  # Features
y = df['Turnout']  # Target variable

# Scale the features to ensure they are within a similar range
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets (assuming 80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict voter turnout for the test data
y_pred = lr_model.predict(X_test)

# Evaluate the model's performance (R-squared)
r_squared = r2_score(y_test, y_pred)
print("R-squared:", r_squared)

# Calculate model accuracy
mse = mean_squared_error(y_test, y_pred)
accuracy = 1 - (mse / y_test.var())
print("Model Accuracy:", accuracy)