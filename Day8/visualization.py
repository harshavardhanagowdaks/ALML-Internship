import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

predictions = model.predict(X)

plt.scatter(X, y)

plt.plot(X, predictions, color="red")

plt.title("Linear Regression")

plt.xlabel("Hours")

plt.ylabel("Marks")

plt.grid(True)

plt.show()