import pandas as pd

df = pd.read_csv("student_dirty.csv")
df.to_csv("cleaned_student.csv", index=False)