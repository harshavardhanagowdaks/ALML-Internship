import pandas as pd
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

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

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions")

print(predictions)

print()

print("Actual Values")

print(y_test.values)

print()

print("Mean Squared Error")

print(mean_squared_error(y_test, predictions))

print()

print("R2 Score")

print(r2_score(y_test, predictions))