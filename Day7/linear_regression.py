import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# Get current folder
current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

# Read dataset
df = pd.read_csv(csv_file)

# Input and Output
X = df[["Hours"]]
y = df["Marks"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

print("Model trained successfully!")