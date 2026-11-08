from sklearn.neighbors import KNeighborsClassifier

# Training data
X = [[1, 2], [2, 3], [3, 3],
     [6, 7], [7, 8], [8, 8]]

# Class labels
y = ['A', 'A', 'A', 'B', 'B', 'B']

# Create KNN model with K = 3
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# Predict the class of a new data point
prediction = model.predict([[2, 2]])

print("Predicted class:", prediction[0])