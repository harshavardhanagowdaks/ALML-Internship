import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=["Hours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.show()