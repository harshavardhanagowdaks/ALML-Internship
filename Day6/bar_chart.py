import pandas as pd
import matplotlib.pyplot as plt
import os

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks - Bar Chart")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()