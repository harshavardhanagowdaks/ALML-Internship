import pandas as pd
import os
import joblib

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

model_path = os.path.join(current_folder, "student_model.pkl")

joblib.dump(model, model_path)

print("Model Saved Successfully!")