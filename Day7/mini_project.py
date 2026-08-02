import pandas as pd
import os
from sklearn.linear_model import LinearRegression

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

print("Dataset")
print(df)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

print(f"Predicted Marks: {prediction[0]:.2f}")