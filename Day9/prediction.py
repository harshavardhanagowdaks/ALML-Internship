import pandas as pd
import os
from sklearn.linear_model import LogisticRegression

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

X = df[["Hours"]]
y = df["Pass"]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[3]])

print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")