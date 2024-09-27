# ☁️ **Weather Prediction Using Naive Bayes Classifier**

### 🔥 **Overview**
This project uses **Naive Bayes** classification to predict the weather based on various features like temperature, humidity, wind speed, and more. It’s implemented in Python using libraries such as **Pandas**, **Scikit-learn**, and **Tkinter** for the user interface. The app displays the prediction in a user-friendly message box.

---

## 🚀 **How it Works**

1. **Data Loading**: The weather data is loaded from a CSV file into a **Pandas DataFrame**.
2. **Feature and Target Split**: The data is split into **features** (X) and the **target variable** (y), where the features are various weather attributes, and the target is the weather prediction.
3. **Training & Testing**: The dataset is divided into **training** and **testing** sets (80/20 split).
4. **Model Creation**: A **Naive Bayes classifier** is trained on the training data to learn the weather patterns.
5. **Prediction**: The trained model makes predictions based on new input data, and the result is displayed in a **Tkinter message box**.
6. **Accuracy Evaluation**: The model’s accuracy is evaluated on the test data and displayed in the terminal.

---

## 🛠️ **Installation Instructions**

### 1. **Clone the Repository**  
Clone this repository to your local machine:
```bash
git clone https://github.com/YourUsername/WeatherPredictionApp.git
```

### 2. **Install Dependencies**  
Ensure you have **Python** installed. Use **pip** to install the required libraries:
```bash
pip install pandas scikit-learn tk
```

### 3. **Prepare the Dataset**  
Make sure the `data.csv` file is available in the same directory as your script. The dataset should have columns like:
- `tempmax`
- `tempmin`
- `temp`
- `feelslikemax`
- `feelslikemin`
- `feelslike`
- `dew`
- `humidity`
- `windspeed`
- `winddir`
- `visibility`
- `predictions` (target variable)

### 4. **Run the Application**  
Once the dataset is ready and dependencies are installed, simply run the script:
```bash
python weather_prediction.py
```

---

## 🖥️ **User Interface**

After running the script, a **message box** will pop up, displaying the predicted weather based on new input data. The message box is enhanced with larger text for easier readability!

---

## 📊 **Model Evaluation**

The accuracy of the Naive Bayes model is printed in the console. The accuracy score helps evaluate how well the model is performing on unseen test data.

---

## 🌟 **Features**

- **Naive Bayes Classifier**: Implements a Gaussian Naive Bayes model for weather prediction.
- **Data Split**: Automatically splits the dataset into training and testing sets (80/20).
- **Tkinter UI**: A simple graphical message box displays the prediction in a user-friendly format.
- **Accuracy Check**: Prints the model's accuracy in the terminal for evaluation.

---

## 💻 **Technology Stack**

- **Python** 🐍
- **Pandas** 🐼
- **Scikit-learn** 🤖
- **Tkinter** 🖥️

---

## ✨ **Future Enhancements**
- Add a **GUI form** to allow users to input weather features directly.
- Incorporate **multiple prediction models** to compare and choose the best fit.
- Allow for **live weather data** input through an API.

---

## 🙌 **Contributing**

Feel free to fork this repository and make contributions. If you find any issues or want to suggest improvements, submit an issue or pull request!

---

Made with ❤️ by **Muhammad Raahim Majid**

