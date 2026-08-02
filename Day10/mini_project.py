import pandas as pd
import os

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

print(df)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))

prediction = model.predict([[hours, attendance]])

if prediction[0] == 1:
    print("\nPrediction: PASS")
else:
    print("\nPrediction: FAIL")

accuracy = accuracy_score(y, model.predict(X))

print("\nAccuracy:", accuracy)