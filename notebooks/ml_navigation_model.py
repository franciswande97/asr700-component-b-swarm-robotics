"""
Machine Learning for Robotic Navigation and Decision-Making.
Trains a lightweight Multi-Layer Perceptron (MLP) classifier to map infrared 
sensor states to discrete navigation actions (Move Forward, Turn Left, Turn Right, Reverse).
Evaluates performance with accuracy metrics and plots a Confusion Matrix.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns

# 1. Simulate dataset representing sensor inputs and navigation actions
# Features: [Front Sensor, Left Sensor, Right Sensor, Rear Sensor]
# Labels: 0 = Move Forward, 1 = Turn Left, 2 = Turn Right, 3 = Reverse
np.random.seed(42)
n_samples = 1000

X = np.random.uniform(0.0, 100.0, size=(n_samples, 4))
y = np.zeros(n_samples, dtype=int)

for i in range(n_samples):
    front, left, right, rear = X[i]
    if front > 70.0:
        y[i] = 3  # Reverse if blocked in front
    elif left > 60.0:
        y[i] = 2  # Turn right if left is blocked
    elif right > 60.0:
        y[i] = 1  # Turn left if right is blocked
    else:
        y[i] = 0  # Move forward clear path

# Add minor noise to simulate real-world sensor stochasticity
noise = np.random.normal(0, 5.0, X.shape)
X = np.clip(X + noise, 0.0, 100.0)

# 2. Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train MLP Classifier (Neural Network)
mlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=42)
mlp.fit(X_train, y_train)

# 4. Evaluate the model
y_pred = mlp.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Test Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Forward', 'Turn Left', 'Turn Right', 'Reverse']))

# 5. Generate and save Confusion Matrix via Matplotlib & Seaborn
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Forward', 'Turn Left', 'Turn Right', 'Reverse'],
            yticklabels=['Forward', 'Turn Left', 'Turn Right', 'Reverse'])
plt.title('ML Navigation Classifier - Confusion Matrix')
plt.xlabel('Predicted Action')
plt.ylabel('True Action')
plt.tight_layout()
plt.savefig('reports/ml_confusion_matrix.png', dpi=300)
plt.show()
print("Confusion matrix plot successfully saved to reports/ml_confusion_matrix.png")