import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the folder where this file is located
current_folder = os.path.dirname(__file__)

# Full path of CSV file
csv_file = os.path.join(current_folder, "student.csv")

# Read CSV
df = pd.read_csv(csv_file)

# Create Line Chart
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Marks"], marker="o")

plt.title("Student Marks - Line Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.grid(True)

plt.show()