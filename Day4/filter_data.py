import pandas as pd

df = pd.read_csv("student.csv")

top_students = df[df["Math"] > 80]

print(top_students)