import pandas as pd
import matplotlib.pyplot as plt
import os

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

plt.figure(figsize=(7,7))

plt.pie(
    df["Marks"],
    labels=df["Name"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Marks Percentage")

plt.show()