import pandas as pd
import os

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

print("Student Dataset")
print(df)

X = df[["Hours"]]
y = df["Pass"]

model = LogisticRegression()

model.fit(X, y)

hours = float(input("Enter Study Hours: "))

prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("\nPrediction: PASS")
else:
    print("\nPrediction: FAIL")

accuracy = accuracy_score(y, model.predict(X))

print("\nModel Accuracy:", accuracy)