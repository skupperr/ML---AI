import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random


PATH_train = 'dataset.csv'
PATH_test = 'dataset_test.csv'
train_dataset = pd.read_csv(PATH_train)
test_dataset = pd.read_csv(PATH_test)

train_dataset['Result'] = train_dataset['Result'].map({'negative': 0, 'positive': 1})
test_dataset['Result'] = test_dataset['Result'].map({'negative': 0, 'positive': 1})

X_train = train_dataset.drop(['Result'],axis=1)
X_train = X_train.to_numpy()
y_train = train_dataset['Result']
y_train = y_train.to_numpy()


X_test = test_dataset.drop(['Result'],axis=1)
X_test = X_test.to_numpy()
y_test = test_dataset['Result']
y_test = y_test.to_numpy()




def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Set number of neighbors
k = 10

# List to store predictions for all test points
predictions = []

# Loop through each test point
for x_test in X_test:
    # Calculate distances from the test point to all training points
    distances = []
    for i in X_train:
        distance = euclidean_distance(i, x_test)
        distances.append(distance)

    # Convert distances to numpy array and sort
    distances = np.asarray(distances)
    distance_indices = np.argsort(distances)

    # Select top-k nearest neighbors
    distance_indices = distance_indices[:k]

    # Initialize label dictionary
    label = dict()
    for unique_label in np.unique(y_train):
        label[unique_label] = 0

    # Count the labels of the nearest neighbors
    for i in distance_indices:
        result = y_train[i]
        label[result] += 1

    # Determine the most frequent label among the neighbors
    predicted_label = max(zip(label.values(), label.keys()))[1]
    predictions.append(predicted_label)

# Print the predictions for all test points
print("Predictions for test set:", predictions)

# Optionally, calculate accuracy
accuracy = np.mean(np.array(predictions) == y_test) * 100
print(f"Accuracy: {accuracy:.2f}%")
