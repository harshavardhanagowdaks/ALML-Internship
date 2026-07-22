import pandas as pd

df = pd.read_csv("student.csv")

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] /3

print(df)

print("\nTop Scorer:")
print(df[df["Average"] == df["Average"].max()])

df.to_csv("student_result.csv", index=False)