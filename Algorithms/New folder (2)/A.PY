import pandas as pd
import numpy as np

PATH_train = 'dataset.csv'
PATH_test = 'test_dataset.csv'

train_dataset = pd.read_csv(PATH_train)
test_dataset = pd.read_csv(PATH_test)

# Extract features and target from the training set
X_train = train_dataset.drop(['Result'], axis=1)
y_train = train_dataset['Result']
y_train = (y_train == 'positive').astype(int)  # Convert to binary (1 = positive, 0 = negative)
X_train = X_train.to_numpy()

# Extract features and IDs from the test set
X_test = test_dataset.drop(['ID'], axis=1) 
test_ids = test_dataset['ID'] 
X_test = X_test.to_numpy()

# Euclidean distance function
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# KNN Prediction function with majority voting
def knn_predict(X_train, y_train, X_test, k=7):
    predictions = []
    for x_test in X_test:
        distances = []
        
        # Calculate the distance between the test point and all training points
        for x_train in X_train:
            distance = euclidean_distance(x_train, x_test)
            distances.append(distance)

        # Convert to numpy array for easier manipulation
        distances = np.array(distances)

        # Get the indices of the k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]

        # Get the labels of the k nearest neighbors
        nearest_labels = y_train[nearest_indices]

        # Majority vote: The most frequent label among the k neighbors
        majority_vote = np.bincount(nearest_labels).argmax()  # This returns the class with the most votes
        predictions.append(majority_vote)
    
    return predictions

# Get predictions (direct binary classification, no probabilities)
predicted_labels = knn_predict(X_train, y_train, X_test, k=7)

# Prepare the output data
output_data = pd.DataFrame({
    'ID': test_ids,
    'TARGET': predicted_labels  # Final predictions (0 or 1)
})

# Save the predictions to a CSV file
output_data.to_csv('predicted_results.csv', index=False)

print("Prediction results saved to 'predicted_results.csv' with binary TARGET values")
