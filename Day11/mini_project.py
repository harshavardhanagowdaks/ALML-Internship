import pandas as pd
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

print(df)

X = df[["Hours","Attendance","Assignments"]]
y = df["Pass"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
assignments = float(input("Assignments Score: "))

prediction = model.predict([[hours,attendance,assignments]])

if prediction[0] == 1:
    print("\nPrediction: PASS")
else:
    print("\nPrediction: FAIL")

accuracy = accuracy_score(y, model.predict(X))

print("\nAccuracy:", accuracy)