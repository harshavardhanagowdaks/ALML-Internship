import pandas as pd

df = pd.read_csv("student.csv")

df["Total"] = df["Math"] + df["Science"] + df["English"]

print(df)