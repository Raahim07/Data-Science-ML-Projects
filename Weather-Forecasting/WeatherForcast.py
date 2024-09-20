import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox

# Load the dataset into a pandas DataFrame
data = pd.read_csv('data.csv')

# Split the data into features (X) and target variable (y)
X = data[['tempmax', 'tempmin', 'temp', 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity', 'windspeed', 
          'winddir', 'visibility']]
y = data['predictions']

# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a Naive-Bayes model and fit it to the training data
model = GaussianNB()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))

# Using trained model to make predictions for new data
new_data = pd.DataFrame({'tempmax': [35.3], 'tempmin': [28.9], 'temp': [31.0], 'feelslikemax': [39.8], 
                         'feelslikemin': [33.5], 'feelslike': [36.5], 'dew': [24.1], 'humidity': [66.5],
                           'windspeed': [30.1], 'winddir': [210.3], 'visibility': [10.0]})
prediction = model.predict(new_data)

# Create a message box to display the predicted weather
root = tk.Tk()
root.withdraw()

# Increase the size of the message box
root.option_add('*Dialog.msg.width', 600)
root.option_add('*Dialog.msg.height', 400)

# Increase the size of the text in the message box
root.option_add('*Dialog.msg.font', 'Helvetica 12')

messagebox.showinfo("Weather Prediction", "The predicted weather is: {}".format(prediction))

# Close the message box and exit the program
root.destroy()
