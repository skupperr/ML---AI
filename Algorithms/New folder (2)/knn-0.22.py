import numpy as np
import pandas as pd

# Load datasets
train_dataset = pd.read_csv('dataset.csv')
test_dataset = pd.read_csv('test_dataset.csv')

# Separate features and labels for training
X_train = train_dataset.drop(['Result'], axis=1).to_numpy(dtype=float)
y_train = (train_dataset['Result'] == 'positive').astype(int)  # Convert to binary labels: 1 for positive, 0 for negative

# Prepare test features (exclude ID)
X_test = test_dataset.drop(['ID'], axis=1).to_numpy(dtype=float)

# Ensure alignment
if X_train.shape[1] != X_test.shape[1]:
    raise ValueError(f"Feature mismatch: Train shape {X_train.shape[1]}, Test shape {X_test.shape[1]}")

# Euclidean distance function
def euclidean_distance(point1, point2):
    point1, point2 = np.array(point1, dtype=float), np.array(point2, dtype=float)
    return np.sqrt(np.sum((point1 - point2) ** 2))

# k-NN prediction function with non-repeating neighbors
def knn_predict(X_train, y_train, X_test, k=7):
    predicted_probabilities = []
    used_indices = set()  # Track used training indices

    for test_point in X_test:
        # Compute distances between test_point and all training points
        distances = np.array([euclidean_distance(train_point, test_point) for train_point in X_train])

        # Get indices sorted by distance, filter out used indices
        sorted_indices = [i for i in distances.argsort() if i not in used_indices]

        # Select the top-k nearest unused neighbors
        nearest_indices = sorted_indices[:k]

        # Add selected indices to the used set
        used_indices.update(nearest_indices)

        # Calculate probability as the mean of neighbors' labels
        probability = np.mean(y_train[nearest_indices]) if nearest_indices else 0.0
        predicted_probabilities.append(probability)

    return np.array(predicted_probabilities)

# Perform predictions on test data
predicted_probabilities = knn_predict(X_train, y_train, X_test, k=7)

# Generate submission file
submission_data = pd.DataFrame({
    'ID': test_dataset['ID'],  # Match ID column
    'TARGET': predicted_probabilities.round()  # Use probabilities as target values
})
submission_data.to_csv('kaggle_submission.csv', index=False)
print("Kaggle submission file created: kaggle_submission.csv")
