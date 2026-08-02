import pandas as pd
import os

from sklearn.model_selection import train_test_split

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data")
print(X_train)

print("\nTesting Data")
print(X_test)