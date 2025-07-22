import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# File paths
PATH_train = 'dataset.csv'
PATH_test = 'test_dataset.csv'

# Load datasets
train_dataset = pd.read_csv(PATH_train)
test_dataset = pd.read_csv(PATH_test)

# Preparing training data
X_train = train_dataset.drop(['Result'], axis=1)
y_train = train_dataset['Result']
y_train = (y_train == 'positive').astype(int)  # Convert to binary (1 = positive, 0 = negative)
X_train = X_train.to_numpy()

# Preparing test data
X_test = test_dataset.drop(['ID'], axis=1)  # Remove ID column for predictions
test_ids = test_dataset['ID']  # Preserve IDs for output
X_test = X_test.to_numpy()

# Define a function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Define k-NN function to calculate probabilities
def knn_predict(X_train, y_train, X_test, k=7):
    predictions = []
    for x_test in X_test:
        distances = []
        for x_train in X_train:
            distance = euclidean_distance(x_train, x_test)
            distances.append(distance)

        # Convert to numpy array
        distances = np.array(distances)

        # Sort and get indices of k-nearest neighbors
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = y_train[nearest_indices]

        # Calculate the probability for the positive class
        prob_positive = np.sum(nearest_labels) / k
        predictions.append(prob_positive)
    return predictions

# Perform predictions on test data
predicted_probabilities = knn_predict(X_train, y_train, X_test, k=7)

# Convert probabilities to binary (0 or 1)
binary_predictions = (np.array(predicted_probabilities) >= 0.5).astype(int)

# Generating the CSV file
output_data = pd.DataFrame({
    'ID': test_ids,
    'TARGET': binary_predictions  # Binary values (0 or 1)
})
output_data.to_csv('predicted_results.csv', index=False)

# Display a message
print("Prediction results saved to 'predicted_results.csv' with binary TARGET values")
