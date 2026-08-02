import pandas as pd
import os

from sklearn.ensemble import RandomForestClassifier

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours", "Attendance", "Assignments"]]
y = df["Pass"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("Random Forest Model Trained Successfully!")