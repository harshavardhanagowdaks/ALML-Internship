import pandas as pd
import os
from sklearn.linear_model import LinearRegression

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[5.5]])

print("Predicted Marks:", prediction[0])