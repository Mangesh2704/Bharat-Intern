#!/usr/bin/env python
# coding: utf-8

# # Iris Flowers Classification using Machine Learning

# In[14]:


#Importing the Dependencies
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont 


# In[15]:


# Loading the Iris dataset
iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                        names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])


# In[16]:


# Mapping species names to numerical values
species_mapping = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
iris_data["species"] = iris_data["species"].map(species_mapping)


# In[17]:


# Selecting features (sepal length and petal length) and the target variable
X = iris_data[["sepal_length", "petal_length"]]
y = iris_data["species"]


# In[18]:


# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training a SVM classifier
svm_classifier = SVC(kernel="linear", C=1)
svm_classifier.fit(X_train, y_train)


# In[19]:


# Main function
class IrisClassificationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Iris Flowers Classification')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        title_label = QLabel('<h1>Iris Flowers Classification</h1>')
        layout.addWidget(title_label)

        self.inputs = {}
        attributes = [
            ("Sepal Length", 4.0, 8.0, 6.0),
            ("Petal Length", 1.0, 7.0, 3.0)
        ]

        for attr, min_val, max_val, init_val in attributes:
            label = QLabel(attr)
            label.setFont(QFont("Poppins", 11, QFont.Bold))
            layout.addWidget(label)
            input_field = QLineEdit(str(init_val))
            layout.addWidget(input_field)
            self.inputs[attr] = input_field

        predict_button = QPushButton('Predict')
        predict_button.setFont(QFont("Arial", 12))
        predict_button.setStyleSheet("background-color: green; color: white;")
        layout.addWidget(predict_button)

        result_label = QLabel()
        result_label.setFont(QFont("Arial", 14, QFont.Bold))
        result_label.setStyleSheet("color: blue;")
        layout.addWidget(result_label)

        self.setLayout(layout)
        self.predict_button = predict_button
        self.result_label = result_label

        self.predict_button.clicked.connect(self.predict_iris_species)

    def predict_iris_species(self):
        sepal_length = float(self.inputs["Sepal Length"].text())
        petal_length = float(self.inputs["Petal Length"].text())

        features = np.array([[sepal_length, petal_length]])
        prediction = svm_classifier.predict(features)

        species_mapping_reverse = {v: k for k, v in species_mapping.items()}
        predicted_species = species_mapping_reverse[prediction[0]]

        self.result_label.setText(f'Predicted Species: {predicted_species}')


def main():
    app = QApplication(sys.argv)
    window = IrisClassificationApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


# In[ ]:




