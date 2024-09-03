# -*- coding: utf-8 -*-
"""FlowerDataSet(Classification).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hyZV0sXt_CA0dLeIU2HDVMCvG1F6Z6wX
"""

print("hello")

import pandas as pd

dataset = pd.read_csv("IRIS.csv")

# getting 5 sample of the dataset
dataset.head()

# Summary statistics
dataset.describe()

# Check for missing values are in dataset
dataset.isnull().sum()

# count rows
dataset['species'].value_counts()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Encode the target variable
label_encoder = LabelEncoder()
label_encoder.fit(dataset['species'])
X = dataset.drop('species', axis=1)
y = dataset['species']
y

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the model
model = DecisionTreeClassifier(random_state=42)
# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

