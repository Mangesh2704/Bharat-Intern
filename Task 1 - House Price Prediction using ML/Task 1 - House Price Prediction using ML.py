#!/usr/bin/env python
# coding: utf-8

# # House Price Prediction using Machine Learning

# In[1]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


# In[3]:


#Loading the Dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

#Training a Linear Regression model
def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model


# In[4]:


# Predicting house price for new data
def predict_price(model, features):
    prediction = model.predict(features)
    return prediction


# In[5]:


# Function to handle prediction button click
def predict():
    new_data = []
    for entry in input_entries:
        value = float(entry.get())
        new_data.append(value)

    new_data = np.array(new_data).reshape(1, -1)
    predicted_price = predict_price(model, new_data)
    formatted_price = f"₹{predicted_price[0]:,.2f}"

    result_label.config(text=f"Predicted House Price: {formatted_price}")


# In[ ]:


# Main function 
def main():
    global model, input_entries, result_label
    window = tk.Tk()
    window.title("House Price Prediction")

    # Load the dataset
    file_path = 'house_data.csv' 
    data = load_data(file_path)

    X = data[['Area', 'No. of Bedrooms', 'Gymnasium', 'Lift Available', 'Car Parking']]
    y = data['Price']

    model = train_model(X, y)

    input_entries = []
    labels = ['Area', 'No. of Bedrooms', 'Gymnasium', 'Lift Available', 'Car Parking']

    for i, label_text in enumerate(labels):
        label = Label(window, text=label_text, font=("Helvetica", 12))
        label.grid(row=i, column=0, padx=10, pady=10)
        entry = Entry(window, font=("Helvetica", 12))
        entry.grid(row=i, column=1, padx=10, pady=10)
        input_entries.append(entry)

    predict_button = Button(window, text="Predict", command=predict, font=("Helvetica", 14), bg="green", fg="white")
    predict_button.grid(row=len(labels), columnspan=2, pady=20)
  
    result_label = Label(window, text="", font=("Helvetica", 16))
    result_label.grid(row=len(labels) + 1, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




