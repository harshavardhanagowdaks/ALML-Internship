import pandas as pd
import matplotlib.pyplot as plt
import os

current_folder = os.path.dirname(__file__)
csv_file = os.path.join(current_folder, "student.csv")

df = pd.read_csv(csv_file)

print("Student Dataset")
print(df)

print("\nHighest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Marks:", df["Marks"].mean())

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Name"], df["Marks"])
plt.title("Student Marks - Scatter Plot")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Pie Chart
plt.figure(figsize=(7,7))
plt.pie(
    df["Marks"],
    labels=df["Name"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Marks Percentage")
plt.show()