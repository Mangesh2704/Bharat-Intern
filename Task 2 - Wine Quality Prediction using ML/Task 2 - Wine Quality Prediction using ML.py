#!/usr/bin/env python
# coding: utf-8

# # Wine Quality Prediction using Machine Learning

# In[ ]:


#Importing the dependencies
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont


# In[ ]:


# Loading the dataset 
data = pd.read_csv('wine_quality.csv')

# Select features and target variable
X = data[[
    "Alcohol",
    "Phenols",
    "Flavanoids",
    "Color.int",
    "Hue",
    "OD",
    "Proline"
]]
y = data["Wine"]


# In[ ]:


# Create a Linear Regression model
model = LinearRegression()
model.fit(X, y)


# In[10]:


#Main Function
class WineQualityPredictionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wine Quality Prediction')
        self.setGeometry(500, 500, 500, 500)

        layout = QVBoxLayout()

        title_label = QLabel('<h1>Wine Quality Prediction</h1>')
        layout.addWidget(title_label)

        description_label = QLabel('Enter the wine attributes to predict its quality:')
        description_label.setFont(QFont("Poppins", 10))
        layout.addWidget(description_label)

        self.inputs = {}
        attributes = [
            ("Alcohol", 10.0, 15.0, 13.0),
            ("Phenols", 0.0, 5.0, 2.0),
            ("Flavanoids", 0.0, 5.0, 2.5),
            ("Color.int", 1.0, 15.0, 5.0),
            ("Hue", 0.0, 3.0, 1.0),
            ("OD", 1.0, 5.0, 3.0),
            ("Proline", 200.0, 2000.0, 1000.0)
        ]

        for attr, min_val, max_val, init_val in attributes:
            label = QLabel(attr)
            label.setFont(QFont("Arial", 11, QFont.Bold))  
            layout.addWidget(label)
            input_field = QLineEdit(str(init_val))
            layout.addWidget(input_field)
            self.inputs[attr] = input_field

        predict_button = QPushButton('Predict')
        predict_button.setFont(QFont("Arial", 12, QFont.Bold))  
        predict_button.setStyleSheet("background-color: green; color: white;")  
        layout.addWidget(predict_button)

        result_label = QLabel()
        result_label.setFont(QFont("Poppins", 14, QFont.Bold))  
        result_label.setStyleSheet("color: green;")  
        layout.addWidget(result_label)

        self.setLayout(layout)

        # Connect the predict button to the prediction function
        predict_button.clicked.connect(self.predict_wine_quality)
        self.result_label = result_label

    def predict_wine_quality(self):
        sample_data = np.array([float(self.inputs[attr].text()) for attr in self.inputs]).reshape(1, -1)
        predicted_quality = model.predict(sample_data)
        self.result_label.setText(f'Predicted Wine Quality: {predicted_quality[0]:.2f}')


def main():
    app = QApplication(sys.argv)
    window = WineQualityPredictionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


# In[ ]:




