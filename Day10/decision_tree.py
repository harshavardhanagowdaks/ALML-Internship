import pandas as pd
import os

from sklearn.tree import DecisionTreeClassifier

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

print("Decision Tree Model Trained Successfully!")