import pandas as pd

df = pd.read_csv("student_dirty.csv")
df = df.dropna()
print(df)