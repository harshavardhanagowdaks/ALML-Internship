import pandas as pd

df = pd.read_csv("student_dirty.csv")

df.rename(columns={"Math":"Mathematics"}, inplace=True)

print(df)
