import pandas as pd
import os

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours"]]
y = df["Pass"]

model = LogisticRegression()

model.fit(X, y)

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Accuracy:", accuracy)