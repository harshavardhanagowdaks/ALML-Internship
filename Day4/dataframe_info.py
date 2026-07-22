import pandas as pd

df = pd.read_csv("student.csv")

print(df.head())
print()

print(df.tail())
print()

print(df.info())
print()

print(df.describe())