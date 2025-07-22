import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

# File paths
PATH_train = 'dataset.csv'
PATH_test = 'test_dataset.csv'

# Load datasets
train_dataset = pd.read_csv(PATH_train)
test_dataset = pd.read_csv(PATH_test)

# Prepare training data
X_train = train_dataset.drop(['Result'], axis=1).select_dtypes(include=[np.number]).to_numpy()
y_train = (train_dataset['Result'] == 'positive').astype(int).to_numpy()  # Convert 'positive'/'negative' to 1/0

# Prepare test data
X_test = test_dataset.drop(['ID'], axis=1).select_dtypes(include=[np.number]).to_numpy()
test_ids = test_dataset['ID']

# Scale the data (scaling isn't mandatory for decision trees, but helps maintain consistency)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the Decision Tree Classifier
decision_tree = DecisionTreeClassifier(max_depth=5, random_state=42)  # max_depth can be adjusted
decision_tree.fit(X_train_scaled, y_train)

# Predict probabilities for the positive class on the test dataset
predicted_probabilities = decision_tree.predict_proba(X_test_scaled)[:, 1]  # Probabilities of the positive class

# Round probabilities to two decimal places
predicted_probabilities_rounded = np.round(predicted_probabilities)

# Create the output DataFrame
output_data = pd.DataFrame({
    'ID': test_ids,
    'TARGET': predicted_probabilities_rounded
})

# Save predictions to CSV
output_file = 'decision_tree_predictions.csv'
output_data.to_csv(output_file, index=False)

print(f"Predictions saved to {output_file}")
