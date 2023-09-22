# Wine Quality Prediction using Machine Learning

## Overview

The Wine Quality Prediction App is a Python application that utilizes machine learning to predict the quality of wine based on its attributes. It employs a Linear Regression model to make predictions. This app provides a user-friendly interface for users to input wine attributes and obtain quality predictions.

## Features

- **User-Friendly Interface:** The app offers a simple and intuitive interface that allows users to input wine attributes conveniently.

- **Predictions:** Users can input various attributes of a wine, such as Alcohol content, Phenols, Flavanoids, Color intensity, Hue, OD (Optical Density), and Proline. The app then uses a trained machine learning model to predict the quality of the wine.

- **Real-Time Feedback:** After entering the wine attributes and clicking the "Predict" button, users receive real-time feedback on the predicted wine quality.

## Getting Started

To run this Wine Quality Prediction App, follow these steps:

1. **Clone the Repository:** Clone this GitHub repository to your local machine.

2. **Install Dependencies:** Ensure you have Python, PyQt5, NumPy, pandas, and scikit-learn installed. You can install them using pip:

    ```
    pip install PyQt5 numpy pandas scikit-learn
    ```

3. **Run the App:** Execute the `wine_quality_app.py` script:

    ```
    python wine_quality_app.py
    ```

4. **Use the App:** Input wine attributes in the provided fields and click the "Predict" button to get quality predictions.

## How It Works

The app employs a Linear Regression model trained on a dataset of wine attributes and quality ratings. When a user inputs the wine attributes and clicks "Predict," the app uses the model to make a prediction and displays the result.

## Technologies Used

- **Python:** The core programming language used for building the app.
  
- **PyQt5:** A Python library for creating graphical user interfaces.
  
- **NumPy:** A library for numerical computations in Python.
  
- **pandas:** A data manipulation library for Python.
  
- **scikit-learn:** A machine learning library for Python.

## Contributions

Contributions to this Wine Quality Prediction App are welcome! If you have ideas for improvements or would like to enhance its functionality, feel free to submit issues or pull requests.

