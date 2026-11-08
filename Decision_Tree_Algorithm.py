from sklearn.tree import DecisionTreeClassifier

X = [
    [2, 60],
    [3, 65],
    [4, 70],
    [6, 80],
    [7, 85],
    [8, 90]
]

y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=0)

model.fit(X, y)

prediction = model.predict([[6, 75]])

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")